# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-17 10:15:01 EDT`
Last processed slot: `early_entry_1015`

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

- Cash: `$65,311.30`
- Equity: `$65,311.30`
- Realized PnL: `$55,311.30`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-17)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   TRI           93.55               31            0.95              0.67        101.02                57.96         0.588          pass              0.680             40.0                           0.488               -5.21             -0.553 downtrend_blocked_slope_and_streak           False                  False
   EXC           92.86               14            0.46              0.14         42.38                15.25         0.551          pass              0.425              0.0                           0.152               -3.01             -0.434 downtrend_blocked_slope_and_streak           False                  False
   WMT           85.29               34            0.46              0.34        107.35                39.87         0.546          pass              0.479             41.0                           0.399                0.87              0.095                                 ok           False                  False
  CHTR           90.24               41            0.64              0.61        134.74                64.77         0.529          pass              0.578             17.1                           0.142              -15.63             -1.342 downtrend_blocked_slope_and_streak           False                  False
  ADSK           87.80               41            0.30              0.47        220.11                56.33         0.528          pass              0.705             81.4                           0.631               -9.14             -0.441 downtrend_blocked_slope_and_streak           False                  False
  ADBE           97.22               36            0.60              1.05        250.05                47.92         0.521          pass              0.837             70.6                           0.620              -11.00             -1.051 downtrend_blocked_slope_and_streak           False                  False
   PEP           88.89               18            0.36              0.34        134.19                14.34         0.521          pass              0.342              0.0                           0.176               -3.73             -0.358            downtrend_blocked_slope           False                  False
  INTU          100.00               32            0.83              1.84        317.34                44.10         0.515          pass              0.715             38.8                           0.254               -8.00             -0.561 downtrend_blocked_slope_and_streak           False                  False
  VRSK           93.10               29            1.11              1.41        181.14                41.00         0.510          pass              0.595             22.6                           0.221               -4.22             -0.331            downtrend_blocked_slope           False                  False
   ADP           96.88               32            0.12              0.23        273.09                24.48         0.506          pass              0.875             92.5                           0.806               -2.33             -0.127                                 ok           False                  False
  CTSH          100.00               38            0.34              0.15         61.79                43.69         0.502          pass              0.860             74.4                           0.561               -2.78             -0.096                                 ok           False                  False
 CMCSA           86.67               15            1.83              0.30         23.60                34.54         0.501          pass              0.266              1.6                           0.156              -13.10             -1.363 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                    detail
2026-09-17T10:15:01.263166-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T10:10:05.493565-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T09:20:04.341541-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                 {'saved': 92, 'empty': 1}
2026-09-16T15:35:01.538068-04:00      manage_1530               exit                                                                                                                                                                                                                                                         {"asset_type": "option", "contract_symbol": "PYPL261016C00055000", "fill_price": 1.116, "pnl": -3434.8, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "PYPL"}
2026-09-16T15:10:01.578825-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-09-16T15:05:01.537613-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-09-16T15:00:06.128176-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-09-16T14:55:02.603343-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-09-16T14:50:31.812161-04:00       entry_1500              entry {"allocated_cash": 34348.0, "asset_type": "option", "contract_symbol": "PYPL261016C00055000", "contracts": 277, "early_entry_score": 0.302, "entry_mode": "regular", "entry_option_price": 1.24, "execution_mode": "option", "matched_signals": 15, "option_liquidity_status": "ok", "option_open_interest": 7856.0, "option_spread_pct": 11.29, "option_volume": 1919.0, "success_rate": 86.67, "ticker": "PYPL", "timing_score": 0.657}
2026-09-16T14:50:31.812161-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                              {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-09-16", "training_samples": 5761, "window": 5}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260917101501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260917101501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260917101501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260917101501)

</details>
