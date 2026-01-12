/** @type {import('tailwindcss').Config} */
export default {
    darkMode: 'class',
    content: [
        "./index.html",
        "./src/**/*.{js,ts,jsx,tsx}",
    ],
    theme: {
        extend: {
            colors: {
                brand: {
                    dark: '#0F172A', // Slate-900 for a more "tooling" feel than pure black
                    blue: '#0B3D91', // Keep classic deep blue
                    orange: '#EA580C', // Orange-600: Professional, less "neon"
                    purple: '#4F46E5', // Indigo-600: More standard SaaS purple
                    surface: 'rgba(15, 23, 42, 0.5)', // Slate based glass
                }
            },
            backgroundImage: {
                'space-gradient': 'radial-gradient(circle at 50% 0%, #1a237e 0%, #050A14 60%)',
                'glass-panel': 'linear-gradient(135deg, rgba(255, 255, 255, 0.05), rgba(255, 255, 255, 0.01))',
            },
            boxShadow: {
                'neon-orange': '0 0 10px rgba(255, 69, 0, 0.5), 0 0 20px rgba(255, 69, 0, 0.3)',
                'neon-blue': '0 0 10px rgba(11, 61, 145, 0.5), 0 0 20px rgba(11, 61, 145, 0.3)',
            }
        },
    },
    plugins: [],
}
