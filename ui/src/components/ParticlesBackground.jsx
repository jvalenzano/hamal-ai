import { useEffect, useMemo, useState } from "react";
import Particles, { initParticlesEngine } from "@tsparticles/react";
import { loadSlim } from "@tsparticles/slim";

const ParticlesBackground = React.memo(() => {
    const [init, setInit] = useState(false);

    // Initialize the tsParticles engine
    useEffect(() => {
        initParticlesEngine(async (engine) => {
            await loadSlim(engine);
        }).then(() => {
            setInit(true);
        });
    }, []);

    const options = useMemo(
        () => ({
            background: {
                color: {
                    value: "transparent", // Let the CSS gradient shine through
                },
            },
            fpsLimit: 120,
            interactivity: {
                detectsOn: "canvas", // Only react when mouse is directly over the background
                events: {
                    onClick: {
                        enable: true,
                        mode: "push",
                    },
                    onHover: {
                        enable: true,
                        mode: "bubble", // Changed to bubble for smoother interaction
                    },
                },
                modes: {
                    bubble: {
                        distance: 200,
                        size: 6,
                        duration: 2,
                        opacity: 0.8,
                        speed: 3
                    },
                    push: {
                        quantity: 4,
                    },
                },
            },
            particles: {
                color: {
                    value: ["#ffffff", "#EA580C"], // White stars + Amber Brand nodes
                },
                links: {
                    color: "#ffffff",
                    distance: 150,
                    enable: true,
                    opacity: 0.15, // Subtle neural web
                    width: 1,
                },
                move: {
                    direction: "none",
                    enable: true,
                    outModes: {
                        default: "out", // Changed from bounce to out for seamless flow
                    },
                    random: true,
                    speed: 0.5, // Slowed down slightly
                    straight: false,
                },
                number: {
                    density: {
                        enable: true,
                        area: 800,
                    },
                    value: 100,
                },
                opacity: {
                    value: { min: 0.1, max: 0.7 },
                    animation: {
                        enable: true,
                        speed: 1,
                        sync: false
                    }
                },
                shape: {
                    type: "circle",
                },
                size: {
                    value: { min: 1, max: 3 },
                },
            },
            detectRetina: true,
        }),
        [],
    );

    if (init) {
        return (
            <Particles
                id="tsparticles"
                className="absolute inset-0 -z-0"
                options={options}
            />
        );
    }

    return <></>;
});

export default ParticlesBackground;
