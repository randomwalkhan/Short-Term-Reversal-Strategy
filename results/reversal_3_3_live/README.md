# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-25 10:15:03 EDT`
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

- Cash: `$73,553.30`
- Equity: `$73,553.30`
- Realized PnL: `$63,553.30`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-25)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  SOXL     option         option SOXL261030C00145000     16          2026-09-24         2026-09-25       20.275      23.775 5600.0   17.262639 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MSTR           92.86               28            2.29              2.59        160.50               109.71         0.694          pass              0.567             11.6                           0.119               20.57              2.798                                 ok            True                  False
  FTNT           84.62               13            2.78              3.48        177.18                58.17         0.572          pass              0.208              2.5                           0.173                9.35              1.051                                 ok            True                  False
   TRI           87.10               31            1.01              0.71        100.02                57.78         0.566          pass              0.624             79.3                           0.519                3.76             -0.116                                 ok            True                  False
  INTC           80.00               30            2.34              2.09        126.49                68.53         0.509          pass              0.184              0.0                           0.163               20.85              2.952                                 ok            True                  False
  CRWD           79.17               24            2.38              4.33        257.82                96.70         0.685          pass              0.212             16.7                           0.181               21.37              2.043                                 ok           False                  False
  MRVL           78.38               37            0.03              0.06        258.92                68.08         0.632          pass              0.243              0.0                           0.163                9.64              1.777                                 ok           False                  False
  PANW           53.85               13            3.55              9.70        385.76                80.20         0.581          pass              0.115             12.3                           0.171               11.10              1.170                                 ok           False                  False
  TEAM          100.00               40            0.37              0.50        192.39                57.21         0.573          pass              0.871             71.3                           0.388                6.86              0.650                                 ok           False                  False
   XEL           90.00               10            0.83              0.41         69.39                16.48         0.555          pass              0.384             20.6                           0.227               -7.79             -0.769 downtrend_blocked_slope_and_streak           False                  False
   KHC           95.00               20            0.42              0.07         23.83                23.05         0.547          pass              0.701             60.0                           0.421               -2.58             -0.322            downtrend_blocked_slope           False                  False
   WBD           93.48               46            0.03              0.01         30.84                38.24         0.532          pass              0.863             83.3                           0.699                9.33              1.161                                 ok           False                  False
  NVDA           91.18               34            0.28              0.44        224.39                44.14         0.524          pass              0.510              0.0                           0.227                2.60              0.666                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-09-25T10:15:03.948523-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-25T10:10:05.955817-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-25T10:05:04.806529-04:00 early_entry_1005 early_entry_shadow {"contract_symbol": "FAST261120C00050000", "current_drop_pct": 0.74, "early_entry_score": 0.835, "early_reclaim_pct": 86.3, "entry_ask": 3.2, "entry_bid": 2.5, "entry_mode": "early", "entry_option_price": 2.85, "hypothetical_budget": 36776.65, "hypothetical_contracts": 129, "matched_signals": 30, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 3441.0, "option_spread_pct": 24.56, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.569, "shadow_only": true, "success_rate": 96.67, "ticker": "FAST", "timing_score": 0.43, "top_candidates": [{"current_drop_pct": 0.74, "early_entry_score": 0.835, "early_reclaim_pct": 86.3, "matched_signals": 30, "recovery_stability_score": 0.569, "success_rate": 96.67, "ticker": "FAST", "timing_score": 0.43, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-25T10:00:06.218962-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-25T09:55:06.037252-04:00      manage_1000               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"asset_type": "option", "contract_symbol": "SOXL261030C00145000", "fill_price": 23.775, "pnl": 5600.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 17.26, "ticker": "SOXL"}
2026-09-25T00:00:05.872425-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {'saved': 92, 'empty': 1}
2026-09-24T15:10:03.736877-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-09-24T15:05:05.616892-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-09-24T15:00:06.644624-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-09-24T14:55:04.772794-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260925101503)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260925101503)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260925101503)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260925101503)

</details>
