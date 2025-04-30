# Query API UI (Frontend)

A lightweight React + Tailwind interface for interacting with the Query API backend.

## Features

- JWT login (admin/password)
- Select & view database entries
- Add new records via form
- Fully responsive UI

## Running Locally

```bash
npm install
npm run dev
```

## Environment Variable

Create a `.env` file:

```env
VITE_API_URL=https://your-api-backend.com
```

## Deploy on Vercel

1. Push this project to GitHub
2. Go to [https://vercel.com](https://vercel.com)
3. Import your repo
4. Set environment variable:
   - `VITE_API_URL=https://your-api-backend.com`
5. Deploy and go live!

## Default Backend Credentials

```
Username: admin
Password: password
```
