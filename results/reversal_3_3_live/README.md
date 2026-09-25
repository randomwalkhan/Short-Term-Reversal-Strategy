# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-25 10:45:06 EDT`
Last processed slot: `early_entry_1045`

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
  MSTR           93.10               29            2.22              2.52        160.53               109.71         0.692          pass              0.588             14.1                           0.298               20.65              2.801                                 ok            True                  False
  CRWD           83.33               30            1.84              3.35        258.23                96.70         0.685          pass              0.397             35.5                           0.429               22.04              2.068                                 ok            True                  False
  TEAM          100.00               39            0.56              0.76        192.28                57.21         0.567          pass              0.820             56.8                           0.376                6.66              0.641                                 ok            True                  False
   TRI           87.10               31            1.15              0.81         99.97                57.78         0.557          pass              0.614             76.4                           0.592                3.62             -0.122                                 ok            True                  False
  FTNT           81.82               11            3.15              3.94        176.98                58.17         0.555          pass              0.121              3.6                           0.194                8.93              1.034                                 ok            True                  False
  NVDA           90.00               30            0.57              0.90        224.20                44.14         0.525          pass              0.487             11.5                           0.154                2.30              0.653                                 ok            True                  False
  SHOP           80.00               20            2.37              2.41        144.13                62.63         0.511          pass              0.174             18.6                           0.321               10.04              1.276                                 ok            True                  False
  INTC           80.65               31            2.15              1.92        126.57                68.53         0.509          pass              0.291             27.6                           0.424               21.09              2.961                                 ok            True                  False
  PANW           60.00               15            3.36              9.18        385.99                80.20         0.587          pass              0.143             17.0                           0.352               11.32              1.179                                 ok           False                  False
   KHC           94.74               19            0.50              0.08         23.82                23.05         0.547          pass              0.667             53.1                           0.450               -2.66             -0.326            downtrend_blocked_slope           False                  False
   XEL           92.31               13            0.79              0.38         69.40                16.48         0.542          pass              0.477             24.7                           0.350               -7.75             -0.767 downtrend_blocked_slope_and_streak           False                  False
   WBD           93.48               46            0.02              0.00         30.84                38.24         0.533          pass              0.888             91.7                           0.770                9.34              1.161                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-09-25T10:45:06.089500-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-25T10:40:06.403638-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-25T10:35:06.003979-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-25T10:30:06.584523-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-25T10:25:05.951093-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-25T10:20:05.036960-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-25T10:15:03.948523-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-25T10:10:05.955817-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-25T10:05:04.806529-04:00 early_entry_1005 early_entry_shadow {"contract_symbol": "FAST261120C00050000", "current_drop_pct": 0.74, "early_entry_score": 0.835, "early_reclaim_pct": 86.3, "entry_ask": 3.2, "entry_bid": 2.5, "entry_mode": "early", "entry_option_price": 2.85, "hypothetical_budget": 36776.65, "hypothetical_contracts": 129, "matched_signals": 30, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 3441.0, "option_spread_pct": 24.56, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.569, "shadow_only": true, "success_rate": 96.67, "ticker": "FAST", "timing_score": 0.43, "top_candidates": [{"current_drop_pct": 0.74, "early_entry_score": 0.835, "early_reclaim_pct": 86.3, "matched_signals": 30, "recovery_stability_score": 0.569, "success_rate": 96.67, "ticker": "FAST", "timing_score": 0.43, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-25T10:00:06.218962-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260925104506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260925104506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260925104506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260925104506)

</details>
