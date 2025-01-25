<a href="https://ai-sql-agent.vercel.app/">
  <video alt="sql-agent-chatbot" src="https://ai-sql-agent.vercel.app/sql-agent.mp4">
</a>
<h1 align="center">SQL Agent AI Chatbot</h1>

`Check the Deployed app :` [`APP`](https://ai-sql-agent.vercel.app/)

`Check the Backend app :` [`BACKEND`](https://github.com/Jayanth-MKV/db-chatapp)

`Check the Demo Video Here :` [`Video`](https://ai-sql-agent.vercel.app/sql-agent.mp4)

## Running locally

You will need to use the environment variables [defined in `.env.example`](.env.example) to run Next.js AI Chatbot. It's recommended you use [Vercel Environment Variables](https://vercel.com/docs/projects/environment-variables) for this, but a `.env` file is all that is necessary.

```bash
pnpm install
pnpm dev
```
or
```bash
npm install
npm run dev
```

Your app template should now be running on [localhost:3000](http://localhost:3000/).


## Key Functionalities
- Natural Language Query Input
- Formatted Display of Query Results
- Responsive Design and attractive UI intgration
- Loader indicating the steps taken by AI Agent
- UI Messages state management
- Error Handling and API Integration

## API endpoints
/api/query - Processes natural language queries and returns data relevant to the input.
/ - chat conversation endpoint
/new - Create a new chat
/auth/* - Paused for now

## Key Challenges Faced
- Handling Streaming Responses:
Managing streaming responses from the backend was complex, as the data needed to be parsed and displayed in the correct format
- Real-Time Updates for Long-Running Queries:
Implementing real-time updates for long-running queries using the Fetch API required careful management of asynchronous operations.
- Implementing the state management and UI messages: This included the integration of the ai/rsc library with the messages of the conversation.

## Future Improvements

- Implement a customizable dashboard where users can save their favorite queries.
- Enable exporting of query results to CSV or Excel formats.
- Implement server-side rendering (SSR) for faster initial load times.
- Add keyboard shortcuts for faster navigation and query submission.
- Implementing charts and graphs for applicable query results would make the data more interpretable.


## Queries That work good:

![ss1](https://ai-sql-agent.vercel.app/ss1.png)
![ss2](https://ai-sql-agent.vercel.app/ss2.png)
![ss3](https://ai-sql-agent.vercel.app/ss3.png)
![ss4](https://ai-sql-agent.vercel.app/ss4.png)
![ss5](https://ai-sql-agent.vercel.app/ss5.png)


## TECH

- [Next.js](https://nextjs.org) App Router
- React Server Components (RSCs), Suspense, and Server Actions
- [Vercel AI SDK](https://sdk.vercel.ai/docs) for streaming chat UI
- Support for custom AI chat models and/or LangChain
- [shadcn/ui](https://ui.shadcn.com)
  - Styling with [Tailwind CSS](https://tailwindcss.com)
  - [Radix UI](https://radix-ui.com) for headless component primitives
  - Icons from [Phosphor Icons](https://phosphoricons.com)
- [NextAuth.js](https://github.com/nextauthjs/next-auth) for authentication
