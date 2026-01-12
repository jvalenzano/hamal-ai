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
                    dark: '#050A14',
                    blue: '#0B3D91',
                    orange: '#FF4500',
                    purple: '#4B0082',
                    surface: 'rgba(11, 61, 145, 0.15)', // Glass effect base
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
