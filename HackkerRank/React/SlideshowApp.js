import React, { useState, useEffect, useRef } from "react";

function Slides({ slides }) {
  const [slideNum, setSlideNum] = useState(0);

  const restartBtn = useRef(null);
  const previousBtn = useRef(null);
  const nextBtn = useRef(null);

  useEffect(() => {
    restartBtn.current.disabled = false;
    previousBtn.current.disabled = false;
    nextBtn.current.disabled = false;
    if (slideNum === 0) {
      restartBtn.current.disabled = true;
      previousBtn.current.disabled = true;
    } else if (slideNum === slides.length - 1) {
      nextBtn.current.disabled = true;
    }
  }, [slideNum, slides.length]);

  const reStart = () => {
    setSlideNum(0);
  };

  const goPrev = () => {
    if (slideNum > 0) setSlideNum(slideNum - 1);
  };

  const goNext = () => {
    if (slideNum < slides.length - 1) setSlideNum(slideNum + 1);
  };

  return (
    <div>
      <div id="navigation" className="text-center">
        <button
          data-testid="button-restart"
          className="small outlined"
          onClick={reStart}
          ref={restartBtn}
        >
          Restart
        </button>
        <button
          data-testid="button-prev"
          className="small"
          onClick={goPrev}
          ref={previousBtn}
        >
          Prev
        </button>
        <button
          data-testid="button-next"
          className="small"
          onClick={goNext}
          ref={nextBtn}
        >
          Next
        </button>
      </div>

      <div id="slide" className="card text-center">
        <h1 data-testid="title">{slides[slideNum].title}</h1>
        <p data-testid="text">{slides[slideNum].text}</p>
      </div>
    </div>
  );
}

export default Slides;
