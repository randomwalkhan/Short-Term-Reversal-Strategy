# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-25 13:24:51 EST`
Last processed slot: `manage_1330`

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

- Cash: `$103,969.80`
- Equity: `$103,969.80`
- Realized PnL: `$93,969.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-11-25)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  REGN           86.11               36            0.66              4.56        985.13                56.69         0.577          pass              0.600             68.7                           0.657                2.31              0.114                                 ok            True                  False
   WMT           86.96               23            0.68              0.63        132.04                24.90         0.529          pass              0.379             17.8                           0.219                4.57              0.390                                 ok            True                  False
  PANW           80.00               40            1.03              2.54        351.90                69.29         0.504          pass              0.504             84.6                           0.824                4.45              1.069                                 ok            True                  False
   APP           88.24               34            1.47              3.92        379.43               128.63         0.774          pass              0.693             78.5                           0.770               -7.23             -1.070 downtrend_blocked_slope_and_streak           False                  False
  INTC           55.00               20            3.80              1.46         54.18               154.72         0.744          pass              0.330             63.2                           0.779              -15.65             -1.309 downtrend_blocked_slope_and_streak           False                  False
  SOXL           66.67               18            8.99              2.05         31.72               318.24         0.721          pass              0.315             63.4                           0.862              -55.07             -7.896            downtrend_blocked_slope           False                  False
  MPWR           59.09               22            2.40             20.01       1181.53               121.95         0.685          pass              0.357             69.5                           0.852              -21.45             -2.192            downtrend_blocked_slope           False                  False
  IDXX           97.78               45            0.01              0.07        712.05                78.73         0.684          pass              0.967             99.4                           0.848                1.34              0.000                                 ok           False                  False
  MCHP           89.19               37            0.18              0.07         56.33                89.73         0.675          pass              0.782             96.6                           0.842               -8.70             -0.850            downtrend_blocked_slope           False                  False
  MRVL           68.18               22            3.51              3.23        130.19               142.93         0.668          pass              0.346             66.5                           0.805              -24.79             -2.703            downtrend_blocked_slope           False                  False
  NVDA           80.00                5            5.25              5.71        152.93               127.00         0.657          pass              0.194             42.6                           0.752              -15.25             -1.414 downtrend_blocked_slope_and_streak           False                  False
  UPRO           80.95               21            1.84              1.52        117.27                94.19         0.635          pass              0.406             81.2                           0.870              -18.31             -2.402 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                    detail
2026-11-25T11:56:08.535993-05:00 early_entry_1155      early_entry_shadow                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-25T10:40:03.209992-05:00 early_entry_1040      early_entry_shadow                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-25T10:06:20.719395-05:00 early_entry_1005      early_entry_shadow                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-25T09:20:10.412914-05:00     data_refresh            data_refresh                                                                                                                                                                                                                 {'saved': 91, 'empty': 2}
2026-11-24T15:10:06.406477-05:00       entry_1500            slot_skipped                                                                                                                                                                                                           {"reason": "already_processed"}
2026-11-24T15:05:05.745009-05:00       entry_1500            slot_skipped                                                                                                                                                                                                           {"reason": "already_processed"}
2026-11-24T15:00:04.642854-05:00       entry_1500            slot_skipped                                                                                                                                                                                                           {"reason": "already_processed"}
2026-11-24T14:55:06.326922-05:00       entry_1500            slot_skipped                                                                                                                                                                                                           {"reason": "already_processed"}
2026-11-24T14:50:04.541007-05:00       entry_1500           entry_skipped                                                                                                                                                                                    {"reason": "no_trade_after_option_and_timing_filters"}
2026-11-24T14:50:04.541007-05:00       entry_1500 entry_candidate_skipped {"early_entry_score": 0.494, "option_liquidity_status": "low_volume", "option_open_interest": 122.0, "option_spread_pct": 8.89, "option_volume": 4.0, "reason": "no_trade_low_option_liquidity", "ticker": "ODFL", "timing_score": 0.512}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261125132451)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261125132451)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261125132451)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261125132451)

</details>
