# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-12 13:50:06 EDT`
Last processed slot: `manage_1400`

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

- Cash: `$27,308.25`
- Equity: `$27,308.25`
- Realized PnL: `$17,308.25`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-06-12)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MPWR           93.94               33            0.58              6.45       1586.79                71.83         0.582          pass              0.795             70.6                           0.446                2.46             -0.338                                 ok            True                  False
  ASML           94.12               34            0.80             10.66       1894.91                60.86         0.522          pass              0.831             80.8                           0.646               15.70              1.330                                 ok            True                   True
  MDLZ           95.45               22            0.88              0.39         63.19                19.17         0.510          pass              0.681             50.0                           0.645                2.87              0.429                                 ok            True                  False
  ISRG           80.77               26            1.18              3.40        411.44                34.54         0.500          pass              0.334             52.3                           0.594               -1.02              0.023                                 ok            True                  False
  INTU           81.25               32            1.38              2.68        275.76               100.42         0.716          pass              0.423             57.0                           0.601              -22.81             -2.207 downtrend_blocked_slope_and_streak           False                  False
   KHC           88.89                9            0.02              0.00         24.22                26.17         0.681          pass              0.595             96.7                           0.594                4.33              0.798                                 ok           False                  False
  AVGO           81.48               27            1.15              3.12        384.23                69.71         0.611          pass              0.358             48.1                           0.484              -17.14             -2.496            downtrend_blocked_slope           False                  False
   PEP          100.00               23            0.04              0.04        143.71                19.04         0.575          pass              0.831             95.5                           0.820                2.59              0.294                                 ok           False                  False
  TEAM           85.29               34            1.41              0.88         88.82                85.01         0.562          pass              0.573             71.7                           0.706              -24.15             -2.622 downtrend_blocked_slope_and_streak           False                  False
  CDNS           95.35               43            0.00              0.01        383.74                58.63         0.555          pass              0.955             99.9                           0.514               -7.35             -0.891            downtrend_blocked_slope           False                  False
  AAPL          100.00               10            1.72              3.56        294.11                23.83         0.532          pass              0.482              9.6                           0.134               -5.15             -0.826            downtrend_blocked_slope           False                  False
  CRWD           82.50               40            0.38              1.85        690.74                64.88         0.519          pass              0.560             80.4                           0.492              -11.93             -1.418 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   detail
2026-06-12T13:30:06.922165-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {'saved': 93}
2026-06-11T16:00:02.840701-04:00      manage_1600               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"asset_type": "option", "contract_symbol": "PAYX260717C00100000", "fill_price": 4.725, "pnl": -1417.5, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "PAYX"}
2026-06-11T15:10:05.901456-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-06-11T15:05:01.637462-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-06-11T15:00:05.308604-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-06-11T14:55:01.789795-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-06-11T14:50:01.795515-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-06-11", "training_samples": 5237, "window": 5}
2026-06-11T14:50:01.795515-04:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"allocated_cash": 14175.0, "asset_type": "option", "contract_symbol": "PAYX260717C00100000", "contracts": 27, "early_entry_score": 0.758, "entry_mode": "regular", "entry_option_price": 5.25, "execution_mode": "option", "matched_signals": 22, "option_liquidity_status": "ok", "option_open_interest": 685.0, "option_spread_pct": 9.52, "option_volume": 131.0, "success_rate": 100.0, "ticker": "PAYX", "timing_score": 0.573}
2026-06-11T11:58:26.585033-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-11T11:22:14.657857-04:00 early_entry_1120 early_entry_shadow {"contract_symbol": "KDP260717C00031000", "current_drop_pct": 0.74, "early_entry_score": 0.82, "early_reclaim_pct": 76.7, "entry_ask": 1.45, "entry_bid": 1.1, "entry_mode": "early", "entry_option_price": 1.275, "hypothetical_budget": 14362.88, "hypothetical_contracts": 112, "matched_signals": 32, "option_liquidity_status": "wide_spread", "option_open_interest": 2194.0, "option_spread_pct": 27.45, "option_volume": 80.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.703, "shadow_only": true, "success_rate": 96.88, "ticker": "KDP", "timing_score": 0.433, "top_candidates": [{"current_drop_pct": 0.74, "early_entry_score": 0.82, "early_reclaim_pct": 76.7, "matched_signals": 32, "recovery_stability_score": 0.703, "success_rate": 96.88, "ticker": "KDP", "timing_score": 0.433, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260612135006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260612135006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260612135006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260612135006)

</details>
