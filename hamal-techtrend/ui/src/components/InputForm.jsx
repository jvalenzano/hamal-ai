import { useState } from 'react'
import { Upload, FileText, ClipboardCopy } from 'lucide-react'

const CHARTER_TEMPLATE = `# Agency Project Charter

## 1. Problem Statement
**What is the core issue?**
[Describe the specific pain point, inefficiency, or gap. Example: "Manual processing takes 3 weeks."]

## 2. Target Audience
**Who is affected?**
[List primary users and stakeholders.]

## 3. Desired Outcome
**Success Metrics:**
[Example: "Reduce processing time to 48 hours."]

## 4. Key Constraints
*   **Compliance:** [e.g., 508, FedRAMP]
*   **Timeline:** [Target delivery date]
`

export default function InputForm({ onSubmit }) {
    const [projectName, setProjectName] = useState('')
    const [charterText, setCharterText] = useState('')
    const [isDragging, setIsDragging] = useState(false)

    const handleDragOver = (e) => {
        e.preventDefault()
        setIsDragging(true)
    }

    const handleDragLeave = (e) => {
        e.preventDefault()
        setIsDragging(false)
    }

    const handleDrop = (e) => {
        e.preventDefault()
        setIsDragging(false)

        const files = e.dataTransfer.files
        if (files.length > 0) {
            const file = files[0]
            if (file.type === "text/plain" || file.name.endsWith(".md") || file.name.endsWith(".txt")) {
                const reader = new FileReader()
                reader.onload = (event) => {
                    setCharterText(event.target.result)
                }
                reader.readAsText(file)
            } else {
                alert("Please upload a .txt or .md file")
            }
        }
    }

    const handleSubmit = async (e) => {
        e.preventDefault()
        onSubmit(projectName || undefined, charterText)
    }

    return (
        <div className="max-w-3xl mx-auto">
            <div className="bg-white dark:bg-gray-800 rounded-lg shadow-sm border border-gray-200 dark:border-gray-700 p-8 transition-colors duration-200">
                <h2 className="text-2xl font-bold text-gray-900 dark:text-white mb-2">
                    Validate Agency Opportunity
                </h2>
                <p className="text-gray-600 dark:text-gray-400 mb-8">
                    Upload charter or paste opportunity description. Validation takes ~15-20 minutes.
                </p>

                <form onSubmit={handleSubmit} className="space-y-6">
                    {/* Project Name */}
                    <div>
                        <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                            Project Name
                        </label>
                        <input
                            type="text"
                            value={projectName}
                            onChange={(e) => setProjectName(e.target.value)}
                            placeholder="e.g., RANGER, TrailWatch"
                            className="w-full px-4 py-2 border border-gray-300 dark:border-gray-600 dark:bg-gray-700 dark:text-white rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent placeholder-gray-400 dark:placeholder-gray-500"
                        />
                    </div>

                    {/* Charter Input */}
                    <div>
                        <div className="flex justify-between items-center mb-2">
                            <label className="block text-sm font-medium text-gray-700 dark:text-gray-300">
                                Opportunity Description
                            </label>
                            <button
                                type="button"
                                onClick={() => setCharterText(CHARTER_TEMPLATE)}
                                className="text-xs text-blue-600 dark:text-blue-400 hover:text-blue-800 dark:hover:text-blue-300 flex items-center gap-1"
                            >
                                <ClipboardCopy className="h-3 w-3" />
                                Use Template
                            </button>
                        </div>
                        <p className="text-xs text-gray-500 dark:text-gray-400 mb-2">
                            Describe the problem, users, and desired outcomes. Be specific about constraints (compliance, legacy systems).
                        </p>
                        <textarea
                            value={charterText}
                            onChange={(e) => setCharterText(e.target.value)}
                            placeholder="Paste agency charter, email, or meeting notes..."
                            rows={12}
                            className="w-full px-4 py-3 border border-gray-300 dark:border-gray-600 dark:bg-gray-700 dark:text-white rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent font-mono text-sm placeholder-gray-400 dark:placeholder-gray-500"
                            required
                        />
                    </div>

                    {/* File Upload (Drag & Drop) */}
                    <div
                        onDragOver={handleDragOver}
                        onDragLeave={handleDragLeave}
                        onDrop={handleDrop}
                        className={`border-2 border-dashed rounded-lg p-6 text-center transition-colors cursor-pointer ${isDragging
                            ? 'border-blue-500 bg-blue-50 dark:bg-blue-900/20'
                            : 'border-gray-300 dark:border-gray-600 hover:border-gray-400 dark:hover:border-gray-500'
                            }`}
                    >
                        <Upload className={`mx-auto h-12 w-12 ${isDragging ? 'text-blue-500' : 'text-gray-400 dark:text-gray-500'}`} />
                        <p className="mt-2 text-sm text-gray-600 dark:text-gray-400">
                            {isDragging ? "Drop file now..." : "Drag and drop charter file (MD, TXT)"}
                        </p>
                        <p className="text-xs text-gray-500 dark:text-gray-500 mt-1">
                            Auto-fills description above
                        </p>
                    </div>

                    {/* Submit */}
                    <button
                        type="submit"
                        disabled={!charterText}
                        className="w-full bg-blue-600 text-white py-3 px-6 rounded-lg font-medium hover:bg-blue-700 disabled:bg-gray-300 dark:disabled:bg-gray-700 disabled:cursor-not-allowed transition-colors"
                    >
                        Run Validation
                    </button>
                </form>
            </div>
        </div>
    )
}
