# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-25 10:20:05 EDT`
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
  MSTR           93.10               29            2.15              2.44        160.57               109.71         0.696          pass              0.596             16.9                           0.167               20.74              2.804                                 ok            True                  False
  CRWD           83.33               30            1.93              3.50        258.17                96.70         0.681          pass              0.388             32.6                           0.288               21.93              2.064                                 ok            True                  False
   TRI           87.10               31            1.02              0.71        100.01                57.78         0.565          pass              0.623             79.0                           0.518                3.75             -0.116                                 ok            True                  False
  FTNT           85.00               20            2.54              3.17        177.31                58.17         0.542          pass              0.309             18.2                           0.211                9.63              1.063                                 ok            True                  False
  INTC           80.00               30            2.39              2.13        126.48                68.53         0.501          pass              0.243             19.8                           0.228               20.80              2.950                                 ok            True                  False
  MRVL           78.38               37            0.20              0.36        258.80                68.08         0.618          pass              0.441             66.4                           0.366                9.46              1.770                                 ok           False                  False
  PANW           57.14               14            3.42              9.33        385.92                80.20         0.586          pass              0.132             15.6                           0.230               11.26              1.176                                 ok           False                  False
   KHC           95.65               23            0.25              0.04         23.84                23.05         0.540          pass              0.769             76.0                           0.659               -2.42             -0.315            downtrend_blocked_slope           False                  False
   WBD           93.48               46            0.02              0.00         30.84                38.24         0.533          pass              0.882             89.7                           0.720                9.34              1.161                                 ok           False                  False
   XEL           93.75               16            0.72              0.35         69.41                16.48         0.530          pass              0.554             31.6                           0.275               -7.68             -0.763 downtrend_blocked_slope_and_streak           False                  False
  NVDA           90.62               32            0.42              0.66        224.30                44.14         0.525          pass              0.533             16.8                           0.242                2.45              0.660                                 ok           False                  False
  CHTR           84.38               32            1.78              1.46        116.92                64.78         0.524          pass              0.408             30.9                           0.535              -17.86             -2.533 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-09-25T10:20:05.036960-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-25T10:15:03.948523-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-25T10:10:05.955817-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-25T10:05:04.806529-04:00 early_entry_1005 early_entry_shadow {"contract_symbol": "FAST261120C00050000", "current_drop_pct": 0.74, "early_entry_score": 0.835, "early_reclaim_pct": 86.3, "entry_ask": 3.2, "entry_bid": 2.5, "entry_mode": "early", "entry_option_price": 2.85, "hypothetical_budget": 36776.65, "hypothetical_contracts": 129, "matched_signals": 30, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 3441.0, "option_spread_pct": 24.56, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.569, "shadow_only": true, "success_rate": 96.67, "ticker": "FAST", "timing_score": 0.43, "top_candidates": [{"current_drop_pct": 0.74, "early_entry_score": 0.835, "early_reclaim_pct": 86.3, "matched_signals": 30, "recovery_stability_score": 0.569, "success_rate": 96.67, "ticker": "FAST", "timing_score": 0.43, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-25T10:00:06.218962-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-25T09:55:06.037252-04:00      manage_1000               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"asset_type": "option", "contract_symbol": "SOXL261030C00145000", "fill_price": 23.775, "pnl": 5600.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 17.26, "ticker": "SOXL"}
2026-09-25T00:00:05.872425-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {'saved': 92, 'empty': 1}
2026-09-24T15:10:03.736877-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-09-24T15:05:05.616892-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-09-24T15:00:06.644624-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260925102005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260925102005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260925102005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260925102005)

</details>
