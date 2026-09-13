import ReactDOM from "https://esm.sh/react-dom@19/client";
import React from "https://esm.sh/react@19";
import { useState, useEffect } from "https://esm.sh/react@19";

const Switch = () => {
  const [isSwitched, setIsSwitched] = useState(() => {
    return sessionStorage.getItem("theme") === "dark";
  });

  useEffect(() => {
    const theme = isSwitched ? "dark" : "light";

    document.documentElement.setAttribute("data-theme", theme); //html
    sessionStorage.setItem("theme", theme);
    
    const block = document.getElementById("block-1");
    //block.setAttribute("data-theme", theme)
    const out = document.querySelector("output");
  //if (card) {
  //  card.style.boxShadow =
  //    theme === "dark"
  //      ? "1pc 5px 50px #141414, 0 5px 6px #0b0a0a;"
  //      : "1pc 5px 50px white, 0 5px 6px white;";
  //}
  if (out) {
    out.style.color =
      theme === "dark"
        ? "white"
        : "black";
  }

  }, [isSwitched]);
    
  return (
    <label
      htmlFor="themeToggle"
      className="themeToggle st-sunMoonThemeToggleBtn"
    >
      <input
        type="checkbox"
        id="themeToggle"
        className="themeToggleInput"
        checked={isSwitched}
        onChange={(e) => setIsSwitched(e.target.checked)}
      />

        <svg width={18} height={18} viewBox="0 0 20 20" fill="currentColor" stroke="none">
          <mask id="moon-mask">
            <rect x={0} y={0} width={20} height={20} fill="white" />
            <circle cx={11} cy={3} r={8} fill="black" />
          </mask>
          <circle className="sunMoon" cx={10} cy={10} r={8} mask="url(#moon-mask)" />
          <g>
            <circle className="sunRay sunRay1" cx={18} cy={10} r="1.5" />
            <circle className="sunRay sunRay2" cx={14} cy="16.928" r="1.5" />
            <circle className="sunRay sunRay3" cx={6} cy="16.928" r="1.5" />
            <circle className="sunRay sunRay4" cx={2} cy={10} r="1.5" />
            <circle className="sunRay sunRay5" cx={6} cy="3.1718" r="1.5" />
            <circle className="sunRay sunRay6" cx={14} cy="3.1718" r="1.5" />
          </g>
        </svg>
          
      </label>

  );
}
          
ReactDOM.createRoot(document.querySelector("Switch")).render(<Switch/>);
