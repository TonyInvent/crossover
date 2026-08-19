# Why an Impedance Curve Never Became a Sound-Pressure Curve

## From the electrical, mechanical, and motional impedance of a loudspeaker to passive crossovers, the Zobel network, and active crossovers

I want to start with a small confession, because every good story starts with one.

For a long time I had a quiet, stubborn confusion about loudspeakers. Every time I looked at the impedance curve of a woofer — a real, honest, measured impedance curve — it looked *awful*. Down near the resonance frequency there was a huge, ugly peak. Above it, the voice-coil inductance made the curve climb again, tilting upward without apology. Put the driver in a vented box and the low end even split into *two* peaks, like a mountain range drawn by someone in a hurry.

None of it looked "flat." It looked like the opposite of flat.

And yet — here is the part that kept me up at night — when I looked at the *frequency response* of the same driver, in the band where it actually plays music, the sound pressure was often quite flat. Smooth. Well behaved.

So the question came out almost by itself:

> If I feed a voltage into a load whose impedance is this lumpy, shouldn't the current lurch up and down with it? And at the mechanical resonance, where the cone is supposedly *easiest* to move, shouldn't the sound pressure bulge along with the impedance? So why doesn't the impedance curve ever turn into a sound-pressure curve?

It sounds like a beginner's question. It is not. Follow it honestly, and it drags you through nearly everything important in loudspeaker design: how current makes force, how a cone moves, how motion generates a back-voltage, how mechanical impedance maps onto electrical impedance, and how sound pressure manages to stay flat anyway. Keep going one more step and you meet the passive crossover. Then the Zobel network. Then the active crossover.

What follows is that journey, told the way I finally understood it — which is to say, the way I wish someone had told it to me: one idea at a time, with the "why" always in view.

---

## 1. First rule: never jump straight from "impedance" to "sound pressure"

The most common mistake is the laziest one. We see

$$Z = \frac{V}{I}$$

and our reflexes fill in the rest: *impedance big, current small, so sound small; impedance small, current big, so sound big.* For a heater — a resistor whose only job is to get warm — that's roughly fine. For a loudspeaker it's simply wrong.

Because a loudspeaker is not an electrical load that happens to be connected to a motor. It *is* a motor. It is a full electromechanical transducer, and the signal runs through a loop:

$$\text{voltage} \rightarrow \text{current} \rightarrow \text{force} \rightarrow \text{motion} \rightarrow \text{air} \rightarrow \text{sound pressure}$$

with a second, backward-running loop on top of it:

$$\text{cone motion} \rightarrow \text{back-EMF} \rightarrow \text{change in current}.$$

So the impedance curve is what you see when you peer into the device through its *electrical terminals only*. The sound-pressure curve is a *different transfer function* — it's what you get when you walk the whole chain from voltage all the way to pressure. The two are related, obviously. But they are not the same function, and treating them as if they were is where every confusion begins.

---

## 2. The loudspeaker's first equation: electricity

Start at the voice coil. If the cone were somehow glued still, the coil would just be a series resistance and inductance:

$$Z_e = R_e + j\omega L_e.$$

So far, boring: an RL load. But the coil sits in a magnetic field, and it *moves*. A conductor moving in a magnetic field generates a voltage, and that voltage is proportional to how fast it moves:

$$e_{\text{bemf}} = Bl \cdot v,$$

where $B$ is the flux density in the gap, $l$ the length of wire in the field, $v$ the coil velocity, and $Bl$ — the "force factor" — is the number that ties the electrical and mechanical worlds together.

So the real electrical equation is not $V = Z_e I$. It is

$$V = Z_e I + Bl\,v.$$

Read that equation slowly, because it is the whole trick in miniature: **the voltage from your amplifier does not all land on the coil's resistance and inductance. A chunk of it is pushed back by the motion of the cone itself.** The moment you accept this, the loudspeaker stops being a resistor and becomes something with a mind of its own.

---

## 3. The second equation: force

Current in a magnetic field feels a force. That's Lorentz:

$$F = Bl\, I.$$

And now look at the symmetry — it's gorgeous. One equation turns current into force:

$$F = Bl\, I,$$

and the other turns velocity into voltage:

$$e = Bl\, v.$$

The same constant $Bl$ sits in both. It is the *gear ratio* between two worlds: electrical on one side, mechanical on the other. If you want one mental image to keep forever, keep this one: **$Bl$ is the transmission between the electrical road and the mechanical road.**

---

## 4. The cone is not free to move however it wants: mechanical impedance

A force is applied. Fine. Now the natural question: *how fast does that force make the cone go?*

And here a wonderful thing happens — the mechanical world starts speaking the same language as the electrical one. Just as electrical impedance is voltage over current,

$$Z_e = \frac{V}{I},$$

mechanical impedance is force over velocity:

$$Z_m = \frac{F}{v}.$$

The correspondence is almost too clean:

$$V \leftrightarrow F, \qquad I \leftrightarrow v.$$

A real cone has at least three mechanical ingredients: its moving mass $M_{ms}$, the losses $R_{ms}$ (the suspension, the spider, the surround), and the compliance $C_{ms}$ of that same suspension acting like a spring. Newton plus Hooke gives

$$M_{ms}\ddot{x} + R_{ms}\dot{x} + \frac{x}{C_{ms}} = F,$$

and in the sinusoidal steady state, with $\dot{x}=v$, this becomes

$$Z_m = R_{ms} + j\omega M_{ms} + \frac{1}{j\omega C_{ms}} = R_{ms} + j\left(\omega M_{ms} - \frac{1}{\omega C_{ms}}\right).$$

Stop and admire this. A mechanical system — mass, spring, friction — has just turned into an *RLC circuit*. Mass looks like an inductor ($j\omega M$). A spring looks like a capacitor ($1/j\omega C$). Friction looks like a resistor. This is not a coincidence and it is not a trick of notation. Both worlds are describing the same thing: *how much "push" is required for a given "flow."* In electricity the flow is current; in mechanics the flow is velocity. Once you see that, a cone and a capacitor are not merely analogous — they are, mathematically, the same animal.

---

## 5. Why the resonance shows up as a giant *electrical* impedance peak

Now the first confusion can die.

Mechanical resonance happens when the mass term and the spring term cancel:

$$\omega_s M_{ms} = \frac{1}{\omega_s C_{ms}} \quad\Rightarrow\quad \omega_s = \frac{1}{\sqrt{M_{ms}C_{ms}}}.$$

At that one frequency, the $+j\omega M_{ms}$ and the $-j/(\omega C_{ms})$ kill each other, and the mechanical impedance collapses to just the losses:

$$Z_m(\omega_s) \approx R_{ms}.$$

If the suspension is good, $R_{ms}$ is small, so the cone is *easy* to move at resonance. Push a little, and it flies. Fine. So here is the paradox: if the cone moves so easily at resonance, why does the *electrical* impedance show a huge peak there?

Precisely *because* it moves so easily.

The cone's velocity $v$ is large, so the back-EMF $Bl v$ is large, and that back-EMF fights the amplifier harder, which *reduces* the input current. Walk it through with the equations. From $Bl I = Z_m v$ we get $v = \frac{Bl}{Z_m}I$. Substitute into $V = Z_e I + Bl v$:

$$V = \left[ Z_e + \frac{(Bl)^2}{Z_m} \right] I,$$

and therefore the input impedance is

$$Z_{\text{in}} = Z_e + \frac{(Bl)^2}{Z_m}.$$

That second term — the **motional impedance** — is the whole story. At resonance $Z_m$ is small, so $(Bl)^2/Z_m$ is enormous, so $Z_{\text{in}}$ is enormous. **The impedance peak is not the cone being stuck. It is the cone being free.** The big peak you see on the chart is the shadow that the mechanical resonance casts onto the electrical port. Read it backwards and the "ugly" curve suddenly has a physical meaning: it is a picture of how much the cone resists motion, reflected through the motor.

---

## 6. But then why doesn't the sound pressure shoot to the sky?

This is the moment where most people get stuck, and it is worth going slowly.

If you drove the speaker with an *ideal constant-current* source, then $v = Bl\,I/Z_m$, and at resonance $Z_m \to R_{ms}$ (small), so the velocity would indeed spike. But a real power amplifier is not a current source. It is close to a *constant-voltage* source with very low output impedance. It holds $V$ fixed, not $I$.

So stop looking at $v/I$ and look at $v/V$ — how much velocity you get *per volt*. Combine the two equations, $V = Z_e I + Bl v$ and $Bl I = Z_m v$:

$$\frac{v}{V} = \frac{Bl}{Z_e Z_m + (Bl)^2}.$$

Now check the resonance. If $Z_m \approx R_{ms}$ and $Z_e R_{ms} \ll (Bl)^2$, then

$$\frac{v}{V} \approx \frac{Bl}{(Bl)^2} = \frac{1}{Bl}.$$

It does *not* blow up as $Z_m \to 0$. Why? Because of a tight, built-in negative feedback loop:

$$v\uparrow \;\Rightarrow\; e_{\text{bemf}}\uparrow \;\Rightarrow\; I\downarrow \;\Rightarrow\; F = Bl I \downarrow.$$

The cone reaches for more motion, and its own back-EMF yanks the current down to stop it. **The loudspeaker brakes itself.** This little feedback loop is, to me, the single most beautiful piece of physics in the whole device — a motor that automatically regulates its own excursion, for free, with no control circuit.

---

## 7. The bigger mystery: why is the midrange so flat?

We have explained why resonance doesn't cause a catastrophe. But there is a deeper, quieter wonder: why is the midrange of an ordinary woofer — tens of Hz to a few kHz — so *flat*?

The answer lives inside the mechanical impedance. Above resonance, $f \gg f_s$, the mass term $\omega M_{ms}$ grows while the spring term $1/(\omega C_{ms})$ shrinks. Their ratio is

$$\frac{\omega M_{ms}}{1/(\omega C_{ms})} = \omega^2 M_{ms} C_{ms} = \left(\frac{f}{f_s}\right)^2.$$

Take a driver with $f_s = 50$ Hz and look at $f = 1$ kHz: the ratio is $(1000/50)^2 = 400$. The mass is already *four hundred times* more important than the spring. So well above resonance,

$$Z_m \approx R_{ms} + j\omega M_{ms} \approx j\omega M_{ms}.$$

This is the **mass-controlled region**, and it is the loudspeaker's happy place.

---

## 8. In the mass-controlled region, the cone actually moves *less*

Follow it through. Ignore the coil inductance for a moment ($Z_e \approx R_e$) and take $Z_m \approx j\omega M_{ms}$:

$$\frac{v}{V} = \frac{Bl}{R_e\, j\omega M_{ms} + (Bl)^2}.$$

Once $\omega M_{ms} R_e \gg (Bl)^2$, this simplifies to

$$\frac{v}{V} \approx \frac{Bl}{j\omega M_{ms} R_e}, \qquad\text{so}\qquad |v| \propto \frac{1}{\omega}.$$

In words: **give a speaker a fixed voltage, and the higher the frequency, the *slower* the cone moves** — down 6 dB for every octave. And the displacement $x$ (since $v = j\omega x$) falls even faster:

$$|x| \propto \frac{1}{\omega^2},$$

down 12 dB per octave.

But wait — this seems to make things *worse*. If the cone moves less and less as frequency rises, why doesn't the sound fall off with it?

---

## 9. Because a loudspeaker does not radiate from displacement — it radiates from *acceleration*

Here is the hinge of the whole argument.

Let $S_d$ be the cone's effective radiating area and $v$ its velocity. The volume velocity — how much air it shoves per second — is

$$U = S_d\, v.$$

For a small piston (small compared to the wavelength), the far-field pressure is proportional to the *rate of change* of that volume velocity:

$$p \propto \frac{j\omega\rho_0}{r} U \propto j\omega S_d v.$$

That $j\omega$ in front is the key. Pressure scales with $\omega v$, not with $v$ alone. And we just found $v \propto 1/\omega$. So

$$p \propto \omega \cdot \frac{1}{\omega} \approx \text{constant}.$$

There it is. The velocity falls with frequency, but the *efficiency with which velocity turns into pressure rises with frequency*, and the two cancel exactly. **That cancellation is the entire reason a normal moving-coil driver has a naturally flat midrange.** The cone moves less, but each unit of motion counts for more.

---

## 10. A more intuitive way to say it: pressure tracks *acceleration*

Since $a = j\omega v$ and $p \propto j\omega S_d v$, we can say it more simply:

$$p \propto S_d\, a.$$

In the mass-controlled region, the story collapses into a beautiful short chain. Fixed voltage $V$ means the current is roughly $I \approx V/R_e$, so the force $F = Bl I$ is roughly constant. In mass control, $F \approx M_{ms} a$, so

$$a \approx \frac{F}{M_{ms}}$$

is roughly constant. And $p \propto S_d a$, so

$$V \rightarrow F \rightarrow a \rightarrow p$$

is one long chain of *constant* proportions. That is why the frequency response is flat. Not because the cone moves a constant amount — it doesn't — but because the *acceleration* is constant, and acceleration is what the air actually feels.

---

## 11. A set of relations worth taping to the wall

For a driver in its mass-controlled, flat-response region, you get four facts that hang together perfectly:

- **Displacement** $x$: $\propto 1/f^2$ (−12 dB/oct)
- **Velocity** $v$: $\propto 1/f$ (−6 dB/oct)
- **Acceleration** $a$: $\approx$ constant (0 dB/oct)
- **Sound pressure** $p$: $\approx$ constant (0 dB/oct)

And these relations explain something every speaker engineer knows in their bones: **why low frequencies eat excursion for breakfast.** To make the same sound pressure at 100 Hz as at 1 kHz, the cone needs roughly

$$\left(\frac{1000}{100}\right)^2 = 100$$

times the displacement. Bass is expensive not mainly in watts, but in *throw*.

---

## 12. Now re-read the impedance curve — there is no contradiction left

The trick is to see that we were never looking at one problem. We were looking at three different questions wearing the same costume.

The input impedance,

$$Z_{\text{in}} = Z_e + \frac{(Bl)^2}{Z_m},$$

answers: *how much current will flow if I apply a voltage?*

The velocity-per-volt,

$$\frac{v}{V} = \frac{Bl}{Z_e Z_m + (Bl)^2},$$

answers: *how fast will the cone move per volt?*

And the pressure-per-volt,

$$\frac{p}{V} \propto \frac{j\omega S_d Bl}{Z_e Z_m + (Bl)^2},$$

answers the question we actually care about: *how much sound do I get per volt?*

An impedance curve that is lumpy and a pressure curve that is flat are not in conflict. **They were never the same function.** One is the view through the electrical port; the other is the view through the whole electro-mechano-acoustic chain. They are allowed to be different shapes. Once you can hold both in your head at once, the "paradox" simply dissolves.

---

## 13. Now, and only now, the passive crossover enters

Everything so far assumed the amplifier drives the driver directly. Now put a passive crossover in between.

Why does the crossover matter *physically*, beyond just "it filters the signal"? Because of the loop we found. The back-EMF has to flow back out of the voice coil and through *whatever circuit the amplifier has put in series with the driver*. If that circuit is the amplifier alone, the amplifier's output impedance is tiny — say $0.05\ \Omega$ — and the back-EMF has a nice low-resistance path home, which lets it generate a strong braking current, which (through $F = Bl I$) produces strong electrical damping. That is what people mean when they say a good amplifier "controls" the driver.

A passive crossover changes that path. And the higher the crossover order, the more it changes it.

---

## 14. First- and second-order crossovers are easy to trust. Fourth-order gets interesting

A first-order low-pass is just a series inductor. At high frequencies its impedance $j\omega L$ grows, the source impedance seen by the driver climbs, and the amplifier's grip loosens. That intuition is correct, and it's enough for a first-order network.

But a real **LR4** — a fourth-order Linkwitz-Riley low-pass, the standard ladder $L_1{-}C_2{-}L_3{-}C_4$ — is a different beast. You can no longer point at one series inductor and call it a day. Short the ideal amplifier's output (which is how you find what the driver "looks back into"), and the source impedance seen from the driver's terminals is

$$Z_s = Z_{C4} \parallel \left[ Z_{L3} + \left( Z_{C2} \parallel Z_{L1} \right) \right].$$

This thing is *wildly* frequency-dependent, and it can develop sharp local peaks — impedance anti-resonances — right where the ladder's reactances cancel.

---

## 15. A counterintuitive concrete example: 1 kHz, 100 ohms

Let me put numbers on it, because a number sticks where a sentence slides off. Take a fourth-order low-pass with

$$L_1 = 1.0\ \text{mH},\quad C_2 = 22\ \mu\text{F},\quad L_3 = 0.47\ \text{mH},\quad C_4 = 4.7\ \mu\text{F}.$$

At $f = 1$ kHz:

$$Z_{L1} = j6.28\ \Omega, \qquad Z_{C2} \approx -j7.23\ \Omega.$$

Nearly equal, opposite signs. Put them in parallel and they nearly cancel into a big impedance:

$$Z_{L1} \parallel Z_{C2} \approx j48\ \Omega,$$

and by the time the rest of the ladder is folded in, the driver looks back and sees

$$|Z_s| \approx 100\ \Omega.$$

At *1 kHz*. In the middle of a woofer's working band. Compare that to the amplifier's own $0.05\ \Omega$, or even to the voice coil's $R_e \approx 3.2\ \Omega$, and the comforting old rule — *"a little extra source resistance is nothing, the coil's own resistance dominates anyway"* — quietly falls apart. At these frequencies, $R_e$ is no longer the big resistor in the loop.

---

## 16. The back-EMF no longer sees an amplifier. It sees a wall.

Follow the braking current. Driven directly, the back-EMF $Bl v$ pushes current roughly $Bl v / R_e$ through a $3.2\ \Omega$ coil — a loop admittance around $0.31$ S. But with the passive network presenting $Z_s \approx -j100\ \Omega$ from the driver's side, the braking current becomes

$$I_{\text{bemf}} = \frac{Bl v}{Z_e + Z_s},$$

which can drop by tens of times. And what actually dissipates mechanical energy is the *real part* of that loop:

$$R_{me}(\omega) = (Bl)^2\, \operatorname{Re}\!\left[ \frac{1}{Z_e + Z_s} \right].$$

If $Z_s$ is mostly reactance, that real part can fall by orders of magnitude. So yes — at certain frequencies, a fourth-order passive crossover genuinely *does* weaken the amplifier's electrical grip on the cone. This isn't "damping factor" marketing folklore; it falls straight out of the electromechanical equations.

---

## 17. Then why doesn't it sound catastrophic in practice?

Here comes the second mystery, and the resolution is as satisfying as the first.

Suppose the active, direct connection gives electrical damping of $15\ \mathrm{N\,s/m}$ and the passive network drops it to $3\ \mathrm{N\,s/m}$ — a factor of five. Sounds like it should be a disaster. But at 1 kHz, a woofer with $f_s$ around 50 Hz is deep in its mass-controlled region:

$$Z_m \approx j\omega M_{ms}.$$

With $M_{ms} = 15$ g at 1 kHz:

$$\omega M_{ms} = 2\pi \cdot 1000 \cdot 0.015 \approx 94\ \mathrm{N\,s/m}.$$

That is a *huge* mechanical impedance. So the total impedance the cone actually fights is $15 + j94$ in one case and $3 + j94$ in the other. The damping changed by 5×, but the *magnitudes* are

$$\sqrt{15^2 + 94^2} \quad\text{vs.}\quad \sqrt{3^2 + 94^2},$$

which are almost identical, because the $j94$ from the mass dominates both. **Damping can change enormously while the steady-state cone motion barely moves.** That distinction is the key to everything that follows.

---

## 18. Electrical damping still matters — just don't confuse it with frequency response

Two systems, $15 + j94$ and $3 + j94$, have nearly the same magnitude. But they are not the same system. The *real part* is what dissipates energy, and the real part differs by 5×. So while the on-axis frequency response may barely twitch, the two systems differ where energy lives and dies:

- transients,
- ringing,
- local mechanical resonances,
- breakup modes,
- certain nonlinear motions.

This is why, when people convert a mature passive speaker to active, the common subjective words are *"cleaner,"* *"faster,"* *"tighter."* Those are not necessarily audiophile mysticism. They are descriptions of a system whose damping changed even though its frequency response didn't. And it's also why you should never claim *"control is ten times better, therefore sound is ten times better"* — because the cone obeys the *total* mechanical impedance, not any one damping term in isolation.

---

## 19. Enter the Zobel network

Now the Zobel finally gets its entrance.

A classic passive crossover often hangs a series R–C network right across the driver's terminals:

$$R_z + C_z,$$

traditionally called a Zobel network or an impedance-compensation network. The textbook explanation is dry: the voice coil has inductance $L_e$, so the impedance rises at high frequencies, while crossover design formulas assume a nice constant load like $4\ \Omega$ or $8\ \Omega$; the Zobel cancels the inductive rise and lets the filter see something closer to a resistor. That explanation is correct, but it sells the Zobel short.

---

## 20. The Zobel is also a *drain path* for the back-EMF

Look at it through the lens we have spent this whole essay building.

If the fourth-order low-pass presents $|Z_s| \approx 100\ \Omega$ to the driver at some frequency, the back-EMF can barely reach the amplifier. But the Zobel is wired *directly across the driver's terminals*. Take $R_z = 6.8\ \Omega$, $C_z = 18\ \mu\text{F}$. At 1 kHz,

$$Z_C = \frac{1}{j\omega C} \approx -j8.8\ \Omega, \qquad Z_z \approx 6.8 - j8.8\ \Omega,$$

a magnitude of only about $11\ \Omega$. So from the back-EMF's point of view, the outside world is no longer the lone $100\ \Omega$ wall; it is

$$Z_{\text{ext}} = Z_s \parallel Z_z \approx 10\ \Omega.$$

Read what just happened: **the Zobel doesn't only flatten the load for the crossover's benefit. It gives the cone's back-EMF a local, low-impedance loop in which to dissipate energy** — cone motion → $Bl v$ → Zobel current → heat in $R_z$. In that light the Zobel is not merely an impedance cosmetic. It is a *passive electromagnetic brake resistor*, quietly bleeding off mechanical energy at the frequencies where the crossover itself has shut the door to the amplifier. That, to me, is the Zobel's real identity.

---

## 21. Finally, what active crossovers actually change

Active (electronic) crossovers are usually described as "replacing the L and C with a DSP." That's true and almost entirely beside the point. The structural change is bigger:

$$\text{passive:}\quad \text{amp} \rightarrow \text{passive crossover} \rightarrow \text{driver}$$

$$\text{active:}\quad \text{DSP} \rightarrow \text{amp} \rightarrow \text{driver}$$

The amplifier moves from *in front of* the filter to *behind* it. Each driver now faces a power amplifier directly, with an output impedance far below $R_e$. For the back-EMF, the return path is no longer an $L{-}C{-}L{-}C$ maze; it is almost exactly

$$R_e + Z_{\text{amp}}, \qquad Z_{\text{amp}} \ll R_e,$$

so $Z_{\text{ext}} \approx 0$. That — not the digital-ness — is the beautiful electrical condition that active crossovers buy you. The frequency splitting happens in the signal world; the electrical-to-mechanical connection is left clean.

---

## 22. Putting the crossover's output impedance into the equations, once and for all

We can now write the single equation that holds everything together. With a frequency-dependent source impedance $Z_s(\omega)$ between the amplifier and the driver:

$$V = \left[Z_e + Z_s\right]I + Bl v, \qquad Bl I = Z_m v,$$

which combine into

$$\frac{v}{V} = \frac{Bl}{\left[Z_e + Z_s\right]Z_m + (Bl)^2},$$

and therefore

$$\frac{p}{V} \propto \frac{j\omega S_d Bl}{\left[Z_e + Z_s\right]Z_m + (Bl)^2}.$$

If this essay has a single equation worth saving, it is this one. Look at everything it gathers into one line: $R_e$ (coil copper), $L_e$ (coil inductance), $Z_s(\omega)$ (amplifier, cables, and the whole passive crossover), $M_{ms}$, $C_{ms}$, $R_{ms}$ (the mechanical side), $Bl$ (the motor), $S_d$ (the radiating area), and the $j\omega$ that converts velocity into pressure. The scattered facts of loudspeaker design are not scattered at all; they are one chain, and this is the chain.

---

## 23. So why doesn't active sound "ten times better" than the theory promises?

This is a genuinely important question, and it deserves a respectful answer rather than a shrug.

On paper, active has an overwhelming list: direct drive, near-zero source impedance, stronger damping, no big power inductors, no capacitor ESR, no load interaction, arbitrary slopes, independent delay, independent EQ, independent level, independent limiting. By every metric it looks like it should be a *rout*.

And yet, take a mature, well-designed passive speaker and convert it to active, and the honest observation is: the sound *changes*, often improves — but not by the world-shattering amount the spec sheet implies. Why?

Because of three layers of dilution we have already met. First, in the driver's main working band, well below the crossover point, the crossover's source impedance is often not that large, so $R_e$ really is still the dominant term in the back-EMF loop. Second, at the frequencies where the crossover's source impedance *does* spike, the driver has entered mass control ($Z_m \approx j\omega M_{ms}$), so a large change in damping barely moves the total impedance magnitude. Third, right at the crossover, the driver is already handing off to its partner, so its weight in the summed response is shrinking. Add Zobel action, the driver's own losses, the box's acoustic load, and the other driver summing on top, and a locally enormous electrical advantage gets smoothed into a much more modest audible change.

The theory is not wrong. It is just that the path from "electrical advantage" to "audible difference" is long, lossy, and full of places where the advantage quietly evaporates.

---

## 24. Which does *not* mean active is a small deal

Quite the opposite. The real prize of active crossovers is not "the same speaker, instantly transformed." It is **design freedom**.

In a passive crossover, everything is entangled. Change one inductor and the magnitude changes, the phase changes, the output impedance changes, the electrical damping changes, the resonance conditions with the next capacitor change, the load seen by the preceding stage changes. A great passive crossover is rarely *calculated*; it is *coaxed* — a designer slowly tuning R, L, C, driver, box, and placement into a good state, one compromise at a time.

An active system breaks the knot. Magnitude alone. Crossover alone. Delay alone. Phase alone. EQ alone. Amplifier direct-coupled. And on top: excursion limiters, thermal limiters, dynamic EQ, per-driver protection, per-box calibration, unit-to-unit compensation, FIR phase correction. The advantage isn't that you will make *this* speaker unrecognizable; it's that you finally get to design the *next* one without wearing handcuffs.

---

## 25. Passive crossovers, looked at again: the art of using your flaws

By this point, a good passive speaker deserves *more* respect, not less.

We started by listing everything wrong with passive crossovers: inductor DCR, capacitor ESR, non-flat driver impedance, non-flat output impedance, twisting phase, mismatched acoustic centers. A beginner wants to delete all of these flaws. A great designer does something subtler: they *fold the flaws into the result*. The driver's natural rolloff gets used. The impedance curve gets used. An inductor's DCR can quietly double as attenuation. A capacitor's interaction with the voice-coil inductance can shape a slope. The Zobel can, in one network, clean up the load *and* give the back-EMF a dissipation path.

The goal was never "a beautiful circuit." It was always "a beautiful sound field." That is why a mature passive crossover can shrink the active-versus-passive gap far more than the raw theory predicts — not because the electrical problems don't exist, but because the designer learned to live *with* them, and turned them into tools.

---

## 26. Back to the question that started all this

Let me close the loop.

> Why is a loudspeaker's impedance curve so lumpy, while its sound-pressure response is so flat?

Now the answer fits in a few sentences. The input impedance

$$Z_{\text{in}} = Z_e + \frac{(Bl)^2}{Z_m}$$

describes what the amplifier sees once the mechanical system has been mirrored back through the back-EMF onto the electrical port. The sound pressure

$$\frac{p}{V} \propto \frac{j\omega S_d Bl}{Z_e Z_m + (Bl)^2}$$

describes what comes out the far end of the whole electro-mechano-acoustic chain. At resonance the cone moves easily, so the back-EMF is strong, so the input current falls, so the electrical impedance peaks. Above resonance the cone is mass-controlled, so $Z_m \approx j\omega M_{ms}$, the velocity falls as $1/\omega$ — but the pressure scales as $\omega v$, so the two cancel and the pressure stays flat. Lumpy impedance, flat pressure: no contradiction at all. They were never the same thing.

---

## 27. The thing to carry in your head is not a curve — it's a loop

If you forget every equation in this essay, keep one picture. Not a chart, but a *loop*:

$$V \rightarrow I \rightarrow Bl\,I \rightarrow Z_m \rightarrow v \rightarrow Bl\,v \rightarrow I,$$

closed, round and round, the electrical and mechanical worlds gripping each other through the motor. And then, branching off the motion into the air:

$$v \rightarrow S_d v \rightarrow j\omega S_d v \rightarrow p.$$

Where does the passive crossover sit? It sits on the $V \rightarrow I$ path. But because the back-EMF must return through that *same* circuit, it also sits on the $v \rightarrow Bl v \rightarrow I$ feedback path. **That is the deep truth: a passive crossover does not merely attenuate voltage at some frequencies. It participates in the loudspeaker's own electromechanical dynamics.** And the active crossover's deepest change is to move the frequency-splitting upstream, into the signal domain, so that each driver once again faces a low-impedance amplifier and the electrical-to-mechanical connection is clean again.

So the whole story can be told in one sentence:

> A passive crossover shapes frequency *inside the power world*, and in doing so it cannot help but enter the driver's electromechanical feedback; an active crossover splits the frequencies *in the signal world first*, then lets the amplifier meet the mechanical world face to face.

That is not "digital beats analog." That is two different *architectures* — and the whole distinction is reachable from one humble, stubborn question:

> *Why is the impedance curve so ugly, when the sound is so flat?*

Follow that question all the way down, and the ugly impedance curve stops being a defect report. It becomes a window. Through it you can finally watch the cone, the magnet, the current, the back-EMF, and the air all pulling on each other — which, it turns out, is what a loudspeaker has been doing the whole time.
