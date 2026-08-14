import { AbsoluteFill, Composition, Interactive } from "remotion";

export const MyComposition = () => {
  return (
    <Composition
      id="MyComp"
      component={MyComponent}
      durationInFrames={60}
      fps={30}
      width={1280}
      height={720}
    />
  );
};

export const MyComponent: React.FC = () => {
  return (
    <AbsoluteFill
      style={{
        backgroundColor: "white",
        alignItems: "center",
        justifyContent: "center",
      }}
    >
      <Interactive.Div
        name="Greeting card"
        style={{ fontSize: 80, padding: 24 }}
      >
        Hello
      </Interactive.Div>
    </AbsoluteFill>
  );
};
