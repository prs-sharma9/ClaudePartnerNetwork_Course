# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository structure

This repository contains a single project:

```
uigen/   # AI-powered React component generator with live preview
```

All development commands must be run from within `uigen/`. See `uigen/CLAUDE.md` for the full command reference, architecture overview, and coding conventions.

## What this project is

`uigen` is a Next.js 15 app that lets users describe React components in a chat interface and see them rendered live. Claude generates JSX/TSX files into an in-memory virtual file system; a client-side Babel pipeline transpiles them and injects the result into a sandboxed iframe — no files are ever written to disk.

Key moving parts:
- **AI layer**: Vercel AI SDK `streamText` with two tools (`str_replace_editor`, `file_manager`) that Claude calls to build and edit virtual files
- **Preview**: `@babel/standalone` transpiles virtual files on the client into blob-URL ES modules rendered in an iframe
- **Persistence**: Prisma + SQLite; authenticated users' projects (messages + virtual FS snapshot) are saved to `uigen/prisma/dev.db`
- **Auth**: JWT in an `httpOnly` cookie; anonymous use is supported but projects are not saved

## Quick start

```bash
cd uigen
npm run setup   # install + prisma generate + migrate
npm run dev     # http://localhost:3000
```
