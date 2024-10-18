import React from 'react';
import ZabbixProblems from './components/ZabbixProblems';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Zabbix Problem Monitoring</h1>
      </header>
      <main>
        <ZabbixProblems />
      </main>
    </div>
  );
}

export default App;
