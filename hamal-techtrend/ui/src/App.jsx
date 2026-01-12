import { useState, useEffect } from 'react'
import { Moon, Sun } from 'lucide-react'
import InputForm from './components/InputForm'
import PipelineProgress from './components/PipelineProgress'
import { PipelineProvider, usePipeline } from './context/PipelineContext'
import './App.css'

function HamalApp() {
  const [view, setView] = useState('input') // 'input' | 'progress'
  const [darkMode, setDarkMode] = useState(false)
  const { startPipeline, projectName } = usePipeline()

  useEffect(() => {
    if (darkMode) {
      document.documentElement.classList.add('dark')
    } else {
      document.documentElement.classList.remove('dark')
    }
  }, [darkMode])

  const handleSubmit = async (name, charterText) => {
    try {
      await startPipeline(charterText, name)
      setView('progress')
    } catch (err) {
      console.error("Failed to start pipeline:", err)
      alert("Failed to start pipeline. Check console.")
    }
  }

  const handleReset = () => {
    setView('input')
  }

  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900 transition-colors duration-200">
      <header className="bg-white dark:bg-gray-800 border-b border-gray-200 dark:border-gray-700 px-8 py-4 transition-colors duration-200">
        <div className="flex items-center justify-between">
          <div className="cursor-pointer" onClick={handleReset}>
            <h1 className="text-2xl font-bold text-gray-900 dark:text-white">
              Hamal <span className="text-gray-500 dark:text-gray-400">@ TechTrend</span>
            </h1>
            <p className="text-sm text-gray-600 dark:text-gray-400">
              AI-Powered Validation Framework
            </p>
          </div>
          <button
            onClick={() => setDarkMode(!darkMode)}
            className="p-2 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-700 text-gray-600 dark:text-gray-300 transition-colors"
          >
            {darkMode ? <Sun className="w-5 h-5" /> : <Moon className="w-5 h-5" />}
          </button>
        </div>
      </header>

      <main className="container mx-auto px-8 py-8 h-[calc(100vh-88px)]">
        {view === 'input' && <InputForm onSubmit={handleSubmit} />}
        {view === 'progress' && (
          <PipelineProgress
            onComplete={() => { }}
          />
        )}
      </main>
    </div>
  )
}

function App() {
  return (
    <PipelineProvider>
      <HamalApp />
    </PipelineProvider>
  )
}

export default App
