// ZabbixProblems.tsx
import React, { useEffect, useState } from 'react';

// Define the shape of the Zabbix problem data
interface ZabbixProblem {
    eventid: string;
    severity: string;
    clock: string;
    name: string;
}

const ZabbixProblems: React.FC = () => {
    // State to hold the list of problems and possible errors
    const [problems, setProblems] = useState<ZabbixProblem[]>([]);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        // Create WebSocket connection to Django Channels
        const ws = new WebSocket('ws://localhost:8000/ws/zabbix/problems/');

        // Handle WebSocket connection opening
        ws.onopen = () => {
            console.log('WebSocket connection established');
        };

        // Handle messages from the WebSocket
        ws.onmessage = (event: MessageEvent) => {
            const data = JSON.parse(event.data);
            console.log("data :", data)
            setProblems(JSON.parse(data));

        //     if (Array.isArray(data)) {
        //         console.log(data)
        //         setProblems(data);
        //     } else {
        //         console.error('Invalid data format received');
        //     }
        };

        // Handle WebSocket errors
        ws.onerror = (err) => {
            console.log(err)
            setError('WebSocket error occurred');
        };

        // Handle WebSocket closure
        ws.onclose = () => {
            console.log('WebSocket connection closed');
        };

        // Cleanup WebSocket connection on component unmount
        return () => ws.close();
    }, []);

    // 

    return (
        <div>
            <h3>Current Zabbix Problems</h3>
            {problems.length === 0 ? (
                <p>No problems detected.</p>
            ) : (
                <ul>
                    {problems.map((problem) => (
                        <li key={problem.eventid}>
                            Name : {problem.name}, Problem ID: {problem.eventid}, Severity: {problem.severity}, Time: {problem.clock}
                        </li>
                    ))}
                </ul>
            )}
        </div>
    );
};

export default ZabbixProblems;
