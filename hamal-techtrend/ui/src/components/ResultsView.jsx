import { useState, useEffect } from 'react'
import ReactMarkdown from 'react-markdown'
import { FileText, Download } from 'lucide-react'

export default function ResultsView({ projectName }) {
    const [activeTab, setActiveTab] = useState('summary')
    const [reports, setReports] = useState({})

    useEffect(() => {
        // Load all markdown reports
        const loadReports = async () => {
            const files = ['problem.md', 'research.md', 'validation.md', 'architecture.md']
            const loaded = {}

            for (const file of files) {
                try {
                    const response = await fetch(`/outputs/${projectName}/${file}`)
                    loaded[file] = await response.text()
                } catch (err) {
                    console.error(`Error loading ${file}:`, err)
                }
            }

            setReports(loaded)
        }

        loadReports()
    }, [projectName])

    const handleExport = () => {
        // Trigger download of all reports as ZIP
        // For POC: just download individual files
        alert('Export feature coming soon')
    }

    return (
        <div className="max-w-6xl mx-auto">
            {/* Header */}
            <div className="bg-white dark:bg-gray-800 rounded-lg shadow-sm border border-gray-200 dark:border-gray-700 p-6 mb-6 transition-colors duration-200">
                <div className="flex items-center justify-between">
                    <div>
                        <h2 className="text-2xl font-bold text-gray-900 dark:text-white">
                            Validation Complete
                        </h2>
                        <p className="text-gray-600 dark:text-gray-400 mt-1">
                            Project: {projectName}
                        </p>
                    </div>
                    <button
                        onClick={handleExport}
                        className="flex items-center gap-2 px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors"
                    >
                        <Download className="w-4 h-4" />
                        Export All Reports
                    </button>
                </div>
            </div>

            {/* Tabs */}
            <div className="bg-white dark:bg-gray-800 rounded-lg shadow-sm border border-gray-200 dark:border-gray-700 transition-colors duration-200">
                <div className="border-b border-gray-200 dark:border-gray-700">
                    <nav className="flex gap-2 px-6">
                        {['summary', 'reports', 'similar'].map(tab => (
                            <button
                                key={tab}
                                onClick={() => setActiveTab(tab)}
                                className={`px-4 py-3 font-medium text-sm border-b-2 transition-colors ${activeTab === tab
                                        ? 'border-blue-600 text-blue-600 dark:border-blue-500 dark:text-blue-400'
                                        : 'border-transparent text-gray-600 dark:text-gray-400 hover:text-gray-900 dark:hover:text-white'
                                    }`}
                            >
                                {tab.charAt(0).toUpperCase() + tab.slice(1)}
                            </button>
                        ))}
                    </nav>
                </div>

                <div className="p-6">
                    {activeTab === 'summary' && (
                        <div>
                            <h3 className="text-xl font-bold text-gray-900 dark:text-white mb-4">
                                Decision Summary
                            </h3>
                            <div className="bg-yellow-50 dark:bg-yellow-900/20 border border-yellow-200 dark:border-yellow-900/50 rounded-lg p-4 mb-6">
                                <p className="text-sm text-yellow-800 dark:text-yellow-200">
                                    <strong>Recommendation:</strong> CONDITIONAL GO (35/50)
                                </p>
                                <p className="text-xs text-yellow-700 dark:text-yellow-300 mt-1">
                                    Review validation.md for conditions before proceeding
                                </p>
                            </div>
                            {/* Add charts/scores here */}
                        </div>
                    )}

                    {activeTab === 'reports' && (
                        <div className="space-y-8">
                            {Object.entries(reports).map(([filename, content]) => (
                                <div key={filename} className="border border-gray-200 dark:border-gray-700 rounded-lg p-6 hover:bg-gray-50 dark:hover:bg-gray-800/50 transition-colors">
                                    <div className="flex items-center gap-2 mb-4">
                                        <FileText className="w-5 h-5 text-gray-600 dark:text-gray-400" />
                                        <h3 className="font-semibold text-gray-900 dark:text-white">{filename}</h3>
                                    </div>
                                    <div className="prose prose-sm max-w-none dark:prose-invert">
                                        <ReactMarkdown>{content}</ReactMarkdown>
                                    </div>
                                </div>
                            ))}
                        </div>
                    )}

                    {activeTab === 'similar' && (
                        <div>
                            <h3 className="text-xl font-bold text-gray-900 dark:text-white mb-4">
                                Similar TechTrend Projects
                            </h3>
                            <p className="text-gray-600 dark:text-gray-400">
                                Reusable components from past projects (from architecture.md)
                            </p>
                        </div>
                    )}
                </div>
            </div>
        </div>
    )
}
