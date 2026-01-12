import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import fs from 'fs'
import path from 'path'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    react(),
    {
      name: 'serve-outputs',
      configureServer(server) {
        server.middlewares.use('/outputs', (req, res, next) => {
          try {
            const root = process.cwd()
            const outputsDir = path.resolve(root, '../outputs')
            const filePath = path.join(outputsDir, req.url)

            if (fs.existsSync(filePath) && fs.statSync(filePath).isFile()) {
              res.setHeader('Content-Type', 'application/json')
              fs.createReadStream(filePath).pipe(res)
            } else {
              res.statusCode = 404
              res.end('Not Found')
            }
          } catch (e) {
            console.error('Middleware error:', e)
            next()
          }
        })
      }
    }
  ],
  server: {
    proxy: {
      '/api': {
        target: 'http://localhost:10000',
        changeOrigin: true,
        secure: false,
      }
    },
    fs: {
      allow: ['..']
    }
  }
})
