import React, { useState, useEffect } from "react";
import { GoogleMap, LoadScript, Marker, HeatmapLayer } from "@react-google-maps/api";
import axios from "axios";

const containerStyle = { width: "100%", height: "500px" };
const center = { lat: 40.7128, lng: -74.0060 };

function MapComponent() {
  const [markers, setMarkers] = useState([]);

  useEffect(() => {
    axios.get("http://127.0.0.1:5000/markers").then((response) => {
      setMarkers(response.data);
    });
  }, []);

  const handleMapClick = (event) => {
    const newMarker = {
      lat: event.latLng.lat(),
      lng: event.latLng.lng(),
      id: Date.now(),
      description: "Suggested park location",
      votes: 0
    };

    setMarkers([...markers, newMarker]);
    axios.post("http://127.0.0.1:5000/add_marker", newMarker);
  };

  const upvoteLocation = (id) => {
    axios.post("http://127.0.0.1:5000/upvote", { id }).then(() => {
      setMarkers((prevMarkers) =>
        prevMarkers.map((marker) =>
          marker.id === id ? { ...marker, votes: marker.votes + 1 } : marker
        )
      );
    });
  };

  return (
    <LoadScript googleMapsApiKey="YOUR_GOOGLE_MAPS_API_KEY">
      <GoogleMap mapContainerStyle={containerStyle} center={center} zoom={12} onClick={handleMapClick}>
        {/* Heatmap Layer */}
        <HeatmapLayer
          data={markers.map(loc => new window.google.maps.LatLng(loc.lat, loc.lng))}
          options={{ radius: 40, opacity: 0.6 }}
        />

        {/* Markers */}
        {markers.map((marker) => (
          <Marker
            key={marker.id}
            position={{ lat: marker.lat, lng: marker.lng }}
            onClick={() => upvoteLocation(marker.id)}
          />
        ))}
      </GoogleMap>
    </LoadScript>
  );
}

export default MapComponent;
