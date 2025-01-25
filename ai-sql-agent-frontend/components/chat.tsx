'use client'

import { cn, nanoid } from '@/lib/utils'
import { ChatList } from '@/components/chat-list'
import { ChatPanel } from '@/components/chat-panel'
import { EmptyScreen } from '@/components/empty-screen'
import { useLocalStorage } from '@/lib/hooks/use-local-storage'
import { useCallback, useEffect, useState } from 'react'
import { useUIState, useAIState } from 'ai/rsc'
import { Message, Session } from '@/lib/types'
import { usePathname, useRouter } from 'next/navigation'
import { useScrollAnchor } from '@/lib/hooks/use-scroll-anchor'
import { toast } from 'sonner'
import { BotMessage } from './stocks'
import { UserMessage } from './stocks/message'

export interface ChatProps extends React.ComponentProps<'div'> {
  initialMessages?: Message[]
  id?: string
  session?: Session
  missingKeys: string[]
}

export function Chat({ id, className, session, missingKeys }: ChatProps) {
  const router = useRouter()
  const path = usePathname()
  // const [input, setInput] = useState('')
  // const [messages] = useUIState()
  // const [aiState] = useAIState()
  const [input, setInput] = useState('')
  const [messages, setMessages] = useUIState()
  const [aiState, setAIState] = useAIState()

  const [_, setNewChatId] = useLocalStorage('newChatId', id)

  useEffect(() => {
    if (session?.user) {
      if (!path.includes('chat') && messages.length === 1) {
        window.history.replaceState({}, '', `/chat/${id}`)
      }
    }
  }, [id, path, session?.user, messages])

  useEffect(() => {
    const messagesLength = aiState.messages?.length
    if (messagesLength === 2) {
      router.refresh()
    }
  }, [aiState.messages, router])

  useEffect(() => {
    setNewChatId(id)
  })

  useEffect(() => {
    missingKeys.map(key => {
      toast.error(`Missing ${key} environment variable!`)
    })
  }, [missingKeys])

  const { messagesRef, scrollRef, visibilityRef, isAtBottom, scrollToBottom } =
    useScrollAnchor()


    const submitUserMessage = async (content: string) => {
      try {
        // const response = await axios.post('http://localhost:8000/mockquery', { question: content });
        
        const response = await fetch(
          "https://db-chatapp.onrender.com/query",
          {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({
              question: content,
            }),
          },
        );
        
        const reader = (response as any).body.getReader();
        const decoder = new TextDecoder();
        let finalResponse = '';
        let isUpdatingLastMessage = false;
    
        while (true) {
          const { done, value } = await reader.read();
          if (done) break;
    
          const chunk = decoder.decode(value, { stream: true });
          const updates = chunk
            .split('\n')
            .filter(Boolean)
            .map(JSON.parse as any);
    
          updates.forEach((update: any) => {
            if (update?.step === 'Final Answer') {
              finalResponse += update?.message;
              isUpdatingLastMessage = false;
            } else {
              isUpdatingLastMessage = true;
              setMessages((prevMessages: any) => [
                ...prevMessages.slice(0, -1),
                {
                  ...prevMessages[prevMessages.length - 1],
                  display: <Loader step={update?.step} message={update?.message} />,
                },
              ]);
            }
          });
        }
        
        setMessages((prevMessages: any) => [
          ...prevMessages.slice(0, -1),
          {
            id: nanoid(),
            display: <BotMessage content={finalResponse} />,
          },
        ]);
      } catch (error) {
        console.error('Error submitting user message:', error);
        setMessages((prevMessages: any) => [
          ...prevMessages,
          {
            id: nanoid(),
            display: <BotMessage content="An error occurred. Please try again later." />,
          },
        ]);
      }
    };

    const handleSubmit = useCallback(async () => {
      if (input.trim() !== '') {
        await submitUserMessage(input);
        setInput('');
      }
    }, [input, setMessages, submitUserMessage]);
    


  return (
    <div
      className="group w-full overflow-auto pl-0 peer-[[data-state=open]]:lg:pl-[250px] peer-[[data-state=open]]:xl:pl-[300px]"
      ref={scrollRef}
    >
      <div
        className={cn('pb-[200px] pt-4 md:pt-10', className)}
        ref={messagesRef}
      >
        {messages.length ? (
          <ChatList messages={messages} isShared={false} session={session} />
        ) : (
          <EmptyScreen />
        )}
        <div className="w-full h-px" ref={visibilityRef} />
      </div>
      <ChatPanel
        id={id}
        input={input}
        setInput={setInput}
        isAtBottom={isAtBottom}
        scrollToBottom={scrollToBottom}
        onSubmit={submitUserMessage}
      />
    </div>
  )
}

export function Loader({ message,step }: { message: string,step:string }) {
  return (
    <>
    <div className="inline-flex items-center gap-1 md:items-center">
      <div className="size-4 animate-spin rounded-full border-2 border-current border-t-transparent"></div>
      <p className="ml-2">{step}</p>
    </div>
      <p className="mt-2">{message}</p>
    </>
  )
}
