import { useState, useEffect } from 'react'
import { CheckCircle2, Loader2, Clock } from 'lucide-react'

export default function ProgressView({ projectName, onComplete }) {
    const [state, setState] = useState(null)
    const [elapsedTime, setElapsedTime] = useState(0)

    useEffect(() => {
        // Poll state.json every 3 seconds
        const pollInterval = setInterval(async () => {
            try {
                const response = await fetch(`/outputs/${projectName}/state.json`)
                const data = await response.json()
                setState(data)

                if (data.status === 'complete') {
                    clearInterval(pollInterval)
                    setTimeout(onComplete, 2000) // Delay before showing results
                }
            } catch (err) {
                console.error('Error polling state:', err)
            }
        }, 3000)

        return () => clearInterval(pollInterval)
    }, [projectName, onComplete])

    useEffect(() => {
        // Update elapsed time
        const timer = setInterval(() => {
            setElapsedTime(t => t + 1)
        }, 1000)
        return () => clearInterval(timer)
    }, [])

    const agents = state?.agents || {}
    const phases = [
        { name: 'Discovery', agent: 'discovery', description: 'Validating problem statement' },
        { name: 'Research', agent: 'research', description: 'Finding precedents & competitors' },
        { name: 'Validation', agent: 'validation', description: 'Scoring feasibility' },
        { name: 'Architecture', agent: 'architecture', description: 'Generating tech stack & costs' }
    ]

    const getPhaseStatus = (agentKey) => {
        const agent = agents[agentKey]
        if (!agent) return 'pending'
        return agent.status // 'running' | 'complete' | 'failed'
    }

    const formatTime = (seconds) => {
        const mins = Math.floor(seconds / 60)
        const secs = seconds % 60
        return `${mins}:${secs.toString().padStart(2, '0')}`
    }

    return (
        <div className="max-w-4xl mx-auto">
            {/* Header */}
            <div className="bg-white dark:bg-gray-800 rounded-lg shadow-sm border border-gray-200 dark:border-gray-700 p-6 mb-6 transition-colors duration-200">
                <div className="flex items-center justify-between">
                    <div>
                        <h2 className="text-2xl font-bold text-gray-900 dark:text-white">
                            Validation in Progress
                        </h2>
                        <p className="text-gray-600 dark:text-gray-400 mt-1">
                            Project: {projectName}
                        </p>
                    </div>
                    <div className="text-right">
                        <div className="flex items-center gap-2 text-gray-600 dark:text-gray-400">
                            <Clock className="w-5 h-5" />
                            <span className="text-lg font-mono">{formatTime(elapsedTime)}</span>
                        </div>
                        <p className="text-sm text-gray-500 dark:text-gray-500 mt-1">
                            Est. 15-20 minutes
                        </p>
                    </div>
                </div>
            </div>

            {/* Progress */}
            <div className="bg-white dark:bg-gray-800 rounded-lg shadow-sm border border-gray-200 dark:border-gray-700 p-6 transition-colors duration-200">
                <div className="space-y-4">
                    {phases.map((phase, idx) => {
                        const status = getPhaseStatus(phase.agent)
                        const agent = agents[phase.agent]

                        return (
                            <div key={phase.agent} className="flex items-start gap-4 p-4 rounded-lg border border-gray-200 dark:border-gray-700">
                                {/* Icon */}
                                <div className="flex-shrink-0 mt-1">
                                    {status === 'complete' && (
                                        <CheckCircle2 className="w-6 h-6 text-green-600 dark:text-green-500" />
                                    )}
                                    {status === 'running' && (
                                        <Loader2 className="w-6 h-6 text-blue-600 dark:text-blue-500 animate-spin" />
                                    )}
                                    {status === 'pending' && (
                                        <Clock className="w-6 h-6 text-gray-400 dark:text-gray-600" />
                                    )}
                                </div>

                                {/* Content */}
                                <div className="flex-grow">
                                    <div className="flex items-center justify-between">
                                        <h3 className="font-semibold text-gray-900 dark:text-white">
                                            Phase {idx + 1}: {phase.name}
                                        </h3>
                                        <span className={`text-xs font-medium px-2 py-1 rounded-full ${status === 'complete' ? 'bg-green-100 text-green-700 dark:bg-green-900/30 dark:text-green-400' :
                                                status === 'running' ? 'bg-blue-100 text-blue-700 dark:bg-blue-900/30 dark:text-blue-400' :
                                                    'bg-gray-100 text-gray-600 dark:bg-gray-700 dark:text-gray-400'
                                            }`}>
                                            {status}
                                        </span>
                                    </div>
                                    <p className="text-sm text-gray-600 dark:text-gray-400 mt-1">
                                        {phase.description}
                                    </p>

                                    {/* Agent output preview (if available) */}
                                    {agent?.output && (
                                        <p className="text-xs text-gray-500 dark:text-gray-500 mt-2">
                                            Output: {agent.output}
                                        </p>
                                    )}
                                </div>
                            </div>
                        )
                    })}
                </div>
            </div>
        </div>
    )
}
