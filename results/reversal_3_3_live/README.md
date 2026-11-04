# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-04 10:35:02 EST`
Last processed slot: `manage_1030`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO + DRAM`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Early-entry mode: `shadow-only`; `10:00 AM-12:00 PM ET` 5-minute scans still log candidates when `early_entry_score >= 0.67`, success rate `>= 88%`, matched signals `>= 30`, early reclaim `>= 60%`, and recovery stability `>= 0.55`, but they do not open positions
- Exit scans: `9:30 AM ET` and every `30` minutes through `4:00 PM ET`; off-hours `5-minute` checkpoints continue mark-to-market updates for open positions, while any legacy share positions still held from older versions continue extended-hours take-profit and stop loss scans until flat
- Live exit ladder: `+15% / +15% / -10%`
- Option entry liquidity gate: `open interest >= 110`, `volume >= 20`, `spread <= 14%`
- Option exit safety: stale option `lastPrice` may be shown for mark-to-market, but take-profit / stop-loss triggers require an executable quote from bid/ask or bid
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- Trend-health gate: block candidates in a short-term down channel when 10d return <= `-1.5%` and either log-slope <= `-0.25%/day` below the 10d lookback average or lower-close streak >= `4`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries use the current option mark price; regular-session stop-loss exits book the planned stop level, with no intraday future path otherwise assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$129,631.55`
- Equity: `$129,631.55`
- Realized PnL: `$119,631.55`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-11-04)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  INTC           58.82               17            3.49              1.48         59.92               129.60         0.740            pass              0.171             16.7                           0.205              -37.14             -4.974            downtrend_blocked_slope           False                  False
  SOXL           65.00               20            5.89              3.02         71.83               167.58         0.567            pass              0.203             26.5                           0.226              -33.35             -3.102            downtrend_blocked_slope           False                  False
  REGN           75.00                4            2.84             19.33        965.08                48.26         0.543            pass              0.096             13.9                           0.189               17.39              2.095                                 ok           False                  False
  DRAM           63.16               19            2.92              0.97         47.22                69.30         0.538            pass              0.176             20.6                           0.201               -5.92             -0.158                                 ok           False                  False
  AVGO           72.00               25            1.24              2.89        330.89                44.04         0.522            pass              0.263             37.1                           0.259               -2.90             -0.041                                 ok           False                  False
  ASML           66.67                9            2.52             27.40       1540.40                44.05         0.522            pass              0.117             21.5                           0.250               -9.64             -0.557            downtrend_blocked_slope           False                  False
  NVDA           77.78               18            1.26              1.83        205.91                32.59         0.508            pass              0.268             54.6                           0.361               -8.06             -0.712 downtrend_blocked_slope_and_streak           False                  False
  LRCX           67.50               40            0.57              0.92        230.32                62.98         0.507            pass              0.495             81.3                           0.474              -12.04             -0.543            downtrend_blocked_slope           False                  False
  SNPS           74.19               31            0.81              2.63        461.75                45.79         0.505            pass              0.281             30.2                           0.277                1.76              0.712                                 ok           False                  False
  INSM           78.95               38            1.01              0.74        104.12                60.46         0.495 below_threshold              0.342             35.4                           0.264                9.94              1.690                                 ok           False                  False
   TXN           90.00               30            0.78              1.71        311.76                35.19         0.493 below_threshold              0.516             22.3                           0.200                9.45              1.046                                 ok           False                  False
  KLAC           71.88               32            1.43              1.56        155.53                57.09         0.491 below_threshold              0.331             44.9                           0.314               -5.79              0.247                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                            detail
2026-11-04T10:35:02.831899-05:00 early_entry_1035 early_entry_shadow                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T10:30:06.151589-05:00 early_entry_1030 early_entry_shadow                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T10:25:06.359695-05:00 early_entry_1025 early_entry_shadow                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T10:20:05.681556-05:00 early_entry_1020 early_entry_shadow                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T10:15:05.290161-05:00 early_entry_1015 early_entry_shadow                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T10:10:06.483796-05:00 early_entry_1010 early_entry_shadow                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T10:05:05.606953-05:00 early_entry_1005 early_entry_shadow                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T10:00:05.152440-05:00 early_entry_1000 early_entry_shadow                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T09:20:05.283761-05:00     data_refresh       data_refresh                                                                                                                                                         {'saved': 91, 'empty': 2}
2026-11-03T16:10:06.665587-05:00      manage_1600               exit {"asset_type": "option", "contract_symbol": "MDLZ261218C00067500", "fill_price": 1.305, "pnl": -6815.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "MDLZ"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261104103502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261104103502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261104103502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261104103502)

</details>
