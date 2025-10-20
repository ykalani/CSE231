import './App.css';
import MapComponent from './MapComponent';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>GreenSpace Mapper</h1>
        <p>Click on the map to suggest new green spaces in your city!</p>
      </header>
      <main>
        <MapComponent />
      </main>
    </div>
  );
}

export default App;
