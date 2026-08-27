# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-27 09:55:06 EDT`
Last processed slot: `manage_1000`

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

- Cash: `$52,788.10`
- Equity: `$52,788.10`
- Realized PnL: `$42,788.10`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-08-27)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  MNST     option         option MNST261016C00048000    140          2026-08-26         2026-08-27         1.95       1.755 -2730.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  AMGN          100.00               18            0.89              2.73        439.17                27.27         0.586          pass              0.692             60.1                           0.676                5.06              0.707                  ok            True                  False
   MAR           96.67               30            0.57              1.43        358.06                33.81         0.551          pass              0.777             63.0                           0.597                1.37              0.115                  ok            True                   True
  COST           92.86               14            1.12              7.47        952.92                18.65         0.550          pass              0.476             17.2                           0.201               -1.71             -0.068                  ok            True                  False
  SBUX           92.86               14            1.00              0.76        108.17                22.90         0.549          pass              0.545             40.3                           0.342               -0.48             -0.007                  ok            True                  False
   KDP           84.62               26            0.92              0.21         32.12                31.04         0.532          pass              0.400             38.9                           0.473                2.54              0.466                  ok            True                  False
  VRTX           97.14               35            0.61              2.34        546.29                33.08         0.528          pass              0.781             53.7                           0.686                5.33              0.772                  ok            True                  False
  PCAR          100.00               21            1.13              1.02        128.79                19.19         0.522          pass              0.562             12.0                           0.173               -2.26             -0.129                  ok            True                  False
  ALNY           85.29               34            0.98              1.64        238.30               130.65         0.521          pass              0.574             73.5                           0.652                4.20              0.563                  ok            True                  False
 CMCSA           94.12               17            1.53              0.29         27.08                26.47         0.518          pass              0.540             21.7                           0.271                2.31              0.466                  ok            True                  False
  MDLZ           92.00               25            0.84              0.37         62.85                22.77         0.510          pass              0.614             47.5                           0.654               -1.65             -0.013                  ok            True                  False
  BKNG           95.00               20            1.97              2.88        207.66                36.49         0.508          pass              0.574             18.9                           0.221               -4.01             -0.094                  ok            True                  False
  NFLX           83.33               18            2.06              1.17         80.96                32.24         0.502          pass              0.261             22.8                           0.228                1.97              0.498                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-08-27T09:50:05.772633-04:00      manage_1000               exit                                                                                                                                                                                                                                                   {"asset_type": "option", "contract_symbol": "MNST261016C00048000", "fill_price": 1.755, "pnl": -2730.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "MNST"}
2026-08-27T00:00:06.493019-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                       {'saved': 93}
2026-08-26T15:50:01.441295-04:00      manage_1600               exit                                                                                                                                                                                                                                                     {"asset_type": "option", "contract_symbol": "LRCX261016C00310000", "fill_price": 31.175, "pnl": 742.5, "reason": "time_exit_at_4pm_scan", "return_pct": 2.72, "ticker": "LRCX"}
2026-08-26T15:10:04.393572-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-08-26T15:05:01.392780-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-08-26T15:00:04.399840-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-08-26T14:55:02.427965-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-08-26T14:50:02.229559-04:00       entry_1500              entry {"allocated_cash": 27300.0, "asset_type": "option", "contract_symbol": "MNST261016C00048000", "contracts": 140, "early_entry_score": 0.298, "entry_mode": "regular", "entry_option_price": 1.95, "execution_mode": "option", "matched_signals": 14, "option_liquidity_status": "ok", "option_open_interest": 249.0, "option_spread_pct": 5.13, "option_volume": 74.0, "success_rate": 85.71, "ticker": "MNST", "timing_score": 1.0}
2026-08-26T14:50:02.229559-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                        {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-08-26", "training_samples": 5704, "window": 5}
2026-08-26T12:00:04.193922-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260827095506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260827095506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260827095506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260827095506)

</details>
