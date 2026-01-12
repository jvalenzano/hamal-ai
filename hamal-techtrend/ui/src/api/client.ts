const API_BASE = import.meta.env.VITE_API_URL || 'http://localhost:10000';

export const apiClient = {
    async triggerPipeline(charterText, projectName) {
        const response = await fetch(`${API_BASE}/api/pipeline/start`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                charter_text: charterText,
                project_name: projectName || undefined,
            }),
        });

        if (!response.ok) {
            throw new Error(`Failed to start pipeline: ${response.statusText}`);
        }

        return await response.json();
    },

    async getPipelineStatus(projectName) {
        const response = await fetch(`${API_BASE}/api/pipeline/${projectName}/status`);
        if (!response.ok) {
            if (response.status === 404) return null; // Not found yet is fine
            throw new Error(`Failed to get status: ${response.statusText}`);
        }
        return await response.json();
    },

    getArtifactUrl(projectName, filename) {
        return `${API_BASE}/api/pipeline/${projectName}/artifacts/${filename}`;
    },

    async getArtifactContent(projectName, filename) {
        const response = await fetch(this.getArtifactUrl(projectName, filename));
        if (!response.ok) {
            const error = new Error(`Failed to get artifact: ${response.statusText}`);
            error.status = response.status;
            throw error;
        }
        return await response.text();
    },

    async getPipelineLogs(projectName) {
        // We treat logs as just another artifact
        try {
            const text = await this.getArtifactContent(projectName, 'activity.log');
            return text;
        } catch (err) {
            if (err.status === 404) return ''; // No logs yet is fine
            console.warn("Log fetch error:", err);
            return '';
        }
    }
};
