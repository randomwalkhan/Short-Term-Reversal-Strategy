# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-10 11:10:04 EDT`
Last processed slot: `manage_1100`

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

- Cash: `$15,257.25`
- Equity: `$30,404.75`
- Realized PnL: `$20,222.25`
- Unrealized PnL: `$182.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CTSH     option         option CTSH260717C00055000       2026-06-09                   1     73     14965.0                 15147.5         2.05           2.08       52.68          52.6          bid_ask_mid                       2.08                bid_ask_mid                    True           182.5                   1.22         93.55               31              0.59         45.34           46.39                  51.28                1420.0           78.0                0.1                      ok
```

## Today's Closed Trades (2026-06-10)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MRVL          100.00               19            2.81              5.25        264.63               141.19         0.666          pass              0.664             46.0                           0.244               30.54              3.518                                 ok            True                  False
  CSCO           96.67               30            0.62              0.53        120.13                60.79         0.627          pass              0.783             62.5                           0.332               -0.05              0.152                                 ok            True                  False
    MU           80.00               25            2.27             14.85        929.53               110.66         0.615          pass              0.323             54.0                           0.275               -1.48             -0.470                                 ok            True                  False
  CTSH           90.32               31            0.57              0.21         52.85                47.83         0.569          pass              0.702             76.6                           0.568               -0.98             -0.405                                 ok            True                   True
  REGN           84.85               33            0.85              3.66        614.61                44.80         0.538          pass              0.464             42.4                           0.340               -2.67             -0.029                                 ok            True                  False
  ISRG           82.35               17            1.66              4.96        424.49                33.80         0.531          pass              0.228             21.8                           0.230                0.23              0.076                                 ok            True                  False
   CSX           92.31               26            0.60              0.20         47.19                21.23         0.516          pass              0.651             54.8                           0.344               -0.00              0.281                                 ok            True                  False
  VRTX           96.15               26            1.03              3.21        444.39                26.58         0.510          pass              0.654             32.2                           0.181                0.91              0.065                                 ok            True                  False
  CDNS           94.29               35            0.82              2.23        389.94                58.96         0.505          pass              0.834             78.6                           0.362                3.65              0.277                                 ok            True                  False
  DRAM          100.00               15            1.43              0.60         59.60               102.89         0.720          pass              0.725             73.1                           0.353               -2.84             -0.822            downtrend_blocked_slope           False                  False
  INTU           71.43               21            2.76              5.67        291.35               101.32         0.680          pass              0.210             23.1                           0.521               -7.16             -1.169 downtrend_blocked_slope_and_streak           False                  False
   TRI           87.88               33            0.01              0.00         82.32                68.38         0.666          pass              0.730             99.8                           0.806                0.18             -0.360                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-06-10T11:10:04.307912-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-10T11:05:01.212784-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-10T11:00:04.519159-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-10T10:55:01.275812-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-10T10:50:04.358355-04:00 early_entry_1050 early_entry_shadow {"contract_symbol": "ABNB260717C00135000", "current_drop_pct": 0.54, "early_entry_score": 0.769, "early_reclaim_pct": 76.2, "entry_ask": 4.45, "entry_bid": 4.2, "entry_mode": "early", "entry_option_price": 4.325, "hypothetical_budget": 7628.63, "hypothetical_contracts": 17, "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 490.0, "option_spread_pct": 5.78, "option_volume": 31.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.608, "shadow_only": true, "success_rate": 91.89, "ticker": "ABNB", "timing_score": 0.431, "top_candidates": [{"current_drop_pct": 0.54, "early_entry_score": 0.769, "early_reclaim_pct": 76.2, "matched_signals": 37, "recovery_stability_score": 0.608, "success_rate": 91.89, "ticker": "ABNB", "timing_score": 0.431, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-06-10T10:45:02.614919-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-10T10:40:02.425306-04:00 early_entry_1040 early_entry_shadow   {"contract_symbol": "WDAY260717C00140000", "current_drop_pct": 0.61, "early_entry_score": 0.782, "early_reclaim_pct": 86.4, "entry_ask": 11.0, "entry_bid": 10.1, "entry_mode": "early", "entry_option_price": 10.55, "hypothetical_budget": 7628.63, "hypothetical_contracts": 7, "matched_signals": 40, "option_liquidity_status": "ok", "option_open_interest": 684.0, "option_spread_pct": 8.53, "option_volume": 78.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.625, "shadow_only": true, "success_rate": 90.0, "ticker": "WDAY", "timing_score": 0.564, "top_candidates": [{"current_drop_pct": 0.61, "early_entry_score": 0.782, "early_reclaim_pct": 86.4, "matched_signals": 40, "recovery_stability_score": 0.625, "success_rate": 90.0, "ticker": "WDAY", "timing_score": 0.564, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-06-10T10:35:05.364684-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-10T10:30:02.359005-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-10T10:25:02.406212-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260610111004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260610111004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260610111004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260610111004)

</details>
