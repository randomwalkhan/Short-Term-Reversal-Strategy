# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-27 11:00:05 EDT`
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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  ABNB           96.55               29            0.91              1.20        187.56                62.05         0.673            pass              0.662             22.6                           0.281                0.66              0.346                      ok            True                  False
   MAR           96.15               26            0.73              1.83        357.89                33.81         0.565            pass              0.721             52.6                           0.574                1.21              0.107                      ok            True                  False
  PCAR          100.00               11            1.69              1.53        128.58                19.19         0.546            pass              0.478              5.4                           0.227               -2.81             -0.155                      ok            True                  False
  ALNY           80.00               20            2.05              3.43        237.53               130.65         0.537            pass              0.254             44.5                           0.564                3.07              0.514                      ok            True                  False
   KDP           86.21               29            0.67              0.15         32.14                31.04         0.530            pass              0.512             55.5                           0.615                2.80              0.477                      ok            True                  False
 CMCSA           92.31               13            2.06              0.39         27.03                26.47         0.510            pass              0.424              8.2                           0.246                1.76              0.442                      ok            True                  False
  MDLZ           89.29               28            0.54              0.24         62.91                22.77         0.506            pass              0.617             66.3                           0.734               -1.35              0.001                      ok            True                  False
  BKNG           96.00               25            1.54              2.25        207.93                36.49         0.503            pass              0.660             36.7                           0.505               -3.59             -0.074                      ok            True                  False
  NFLX           80.00               15            2.34              1.34         80.89                32.24         0.500 below_threshold              0.119             12.0                           0.200                1.67              0.484                      ok            True                  False
  MNST           71.43                7            2.22              0.74         47.49               551.93         1.000            pass              0.168             22.6                           0.521                0.15              0.334                      ok           False                  False
  INSM           89.66               29            1.52              1.32        123.82               110.38         0.789            pass              0.555             30.5                           0.462               -3.03             -0.316 downtrend_blocked_slope           False                  False
   WMT          100.00                8            1.74              1.27        103.79                39.06         0.642            pass              0.500             12.1                           0.269              -11.19             -1.334 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           detail
2026-08-27T11:00:05.720063-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-27T10:55:01.790895-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                           {"contract_symbol": "IDXX261016C00550000", "current_drop_pct": 0.56, "early_entry_score": 0.675, "early_reclaim_pct": 63.0, "entry_ask": 26.8, "entry_bid": 22.7, "entry_mode": "early", "entry_option_price": 24.75, "hypothetical_budget": 26394.05, "hypothetical_contracts": 10, "matched_signals": 38, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 7.0, "option_spread_pct": 16.57, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.632, "shadow_only": true, "success_rate": 89.47, "ticker": "IDXX", "timing_score": 0.468, "top_candidates": [{"current_drop_pct": 0.56, "early_entry_score": 0.675, "early_reclaim_pct": 63.0, "matched_signals": 38, "recovery_stability_score": 0.632, "success_rate": 89.47, "ticker": "IDXX", "timing_score": 0.468, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-27T10:50:01.751368-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                              {"contract_symbol": "MAR261016C00360000", "current_drop_pct": 0.53, "early_entry_score": 0.752, "early_reclaim_pct": 65.4, "entry_ask": 12.6, "entry_bid": 10.7, "entry_mode": "early", "entry_option_price": 11.65, "hypothetical_budget": 26394.05, "hypothetical_contracts": 22, "matched_signals": 31, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 214.0, "option_spread_pct": 16.31, "option_volume": 3.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.633, "shadow_only": true, "success_rate": 93.55, "ticker": "MAR", "timing_score": 0.542, "top_candidates": [{"current_drop_pct": 0.53, "early_entry_score": 0.752, "early_reclaim_pct": 65.4, "matched_signals": 31, "recovery_stability_score": 0.633, "success_rate": 93.55, "ticker": "MAR", "timing_score": 0.542, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-27T10:45:02.873607-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                           {"contract_symbol": "GEHC261002C00073000", "current_drop_pct": 0.53, "early_entry_score": 0.832, "early_reclaim_pct": 70.4, "entry_ask": 2.8, "entry_bid": 2.25, "entry_mode": "early", "entry_option_price": 2.525, "hypothetical_budget": 26394.05, "hypothetical_contracts": 104, "matched_signals": 36, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 1.0, "option_spread_pct": 21.78, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.745, "shadow_only": true, "success_rate": 97.22, "ticker": "GEHC", "timing_score": 0.477, "top_candidates": [{"current_drop_pct": 0.53, "early_entry_score": 0.832, "early_reclaim_pct": 70.4, "matched_signals": 36, "recovery_stability_score": 0.745, "success_rate": 97.22, "ticker": "GEHC", "timing_score": 0.477, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-27T10:40:06.542712-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                 {"contract_symbol": "GEHC261002C00073000", "current_drop_pct": 0.58, "early_entry_score": 0.817, "early_reclaim_pct": 67.3, "entry_ask": 2.8, "entry_bid": 2.2, "entry_mode": "early", "entry_option_price": 2.5, "hypothetical_budget": 26394.05, "hypothetical_contracts": 105, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 1.0, "option_spread_pct": 24.0, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.698, "shadow_only": true, "success_rate": 97.14, "ticker": "GEHC", "timing_score": 0.48, "top_candidates": [{"current_drop_pct": 0.58, "early_entry_score": 0.817, "early_reclaim_pct": 67.3, "matched_signals": 35, "recovery_stability_score": 0.698, "success_rate": 97.14, "ticker": "GEHC", "timing_score": 0.48, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-27T10:35:01.793771-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                           {"contract_symbol": "GEHC261002C00073000", "current_drop_pct": 0.59, "early_entry_score": 0.809, "early_reclaim_pct": 66.9, "entry_ask": 2.75, "entry_bid": 2.15, "entry_mode": "early", "entry_option_price": 2.45, "hypothetical_budget": 26394.05, "hypothetical_contracts": 107, "matched_signals": 34, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 1.0, "option_spread_pct": 24.49, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.652, "shadow_only": true, "success_rate": 97.06, "ticker": "GEHC", "timing_score": 0.486, "top_candidates": [{"current_drop_pct": 0.59, "early_entry_score": 0.809, "early_reclaim_pct": 66.9, "matched_signals": 34, "recovery_stability_score": 0.652, "success_rate": 97.06, "ticker": "GEHC", "timing_score": 0.486, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-27T10:30:01.239730-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-27T10:25:01.830320-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-27T10:20:01.828046-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                            {"contract_symbol": "GILD261016C00145000", "current_drop_pct": 0.55, "early_entry_score": 0.841, "early_reclaim_pct": 78.5, "entry_ask": 7.55, "entry_bid": 6.95, "entry_mode": "early", "entry_option_price": 7.25, "hypothetical_budget": 26394.05, "hypothetical_contracts": 36, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 1162.0, "option_spread_pct": 8.28, "option_volume": 32.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.68, "shadow_only": true, "success_rate": 94.44, "ticker": "GILD", "timing_score": 0.467, "top_candidates": [{"current_drop_pct": 0.55, "early_entry_score": 0.841, "early_reclaim_pct": 78.5, "matched_signals": 36, "recovery_stability_score": 0.68, "success_rate": 94.44, "ticker": "GILD", "timing_score": 0.467, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-27T10:15:02.591060-04:00 early_entry_1015 early_entry_shadow {"contract_symbol": "REGN261016C00810000", "current_drop_pct": 0.63, "early_entry_score": 0.836, "early_reclaim_pct": 84.7, "entry_ask": 41.0, "entry_bid": 32.7, "entry_mode": "early", "entry_option_price": 36.85, "hypothetical_budget": 26394.05, "hypothetical_contracts": 7, "matched_signals": 30, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 34.0, "option_spread_pct": 22.52, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.661, "shadow_only": true, "success_rate": 100.0, "ticker": "REGN", "timing_score": 0.486, "top_candidates": [{"current_drop_pct": 0.63, "early_entry_score": 0.836, "early_reclaim_pct": 84.7, "matched_signals": 30, "recovery_stability_score": 0.661, "success_rate": 100.0, "ticker": "REGN", "timing_score": 0.486, "trend_health_status": "ok"}, {"current_drop_pct": 0.52, "early_entry_score": 0.802, "early_reclaim_pct": 60.8, "matched_signals": 35, "recovery_stability_score": 0.675, "success_rate": 97.14, "ticker": "VRTX", "timing_score": 0.534, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260827110005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260827110005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260827110005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260827110005)

</details>
