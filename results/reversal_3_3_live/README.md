# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-30 15:50:05 EDT`
Last processed slot: `manage_1600`

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

- Cash: `$58,976.55`
- Equity: `$117,626.55`
- Realized PnL: `$107,176.55`
- Unrealized PnL: `$450.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   CEG     option         option CEG261218C00260000       2026-10-30                   0     30     58200.0                 58650.0         19.4          19.55      259.39         262.3          bid_ask_mid                      19.55                bid_ask_mid                    True           450.0                   0.77          84.0               25              1.96         51.59           49.61                  64.38                 503.0           30.0               0.08                      ok
```

## Today's Closed Trades (2026-10-30)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price      pnl  return_pct           exit_reason
  MSTR     option         option MSTR261218C00140000     41          2026-10-29         2026-10-30       15.025     13.5225 -6160.25       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   CEG           87.50               32            0.91              1.68        263.86                64.38         0.608            pass              0.617             69.7                           0.673               -3.39             -0.236                                 ok            True                  False
  FAST           91.67               12            1.05              0.38         52.38                21.92         0.554            pass              0.441             20.3                           0.293                2.44              0.201                                 ok            True                  False
  SBUX           84.62               13            1.63              1.20        105.00                26.25         0.515            pass              0.337             47.6                           0.379                6.43              0.738                                 ok            True                  False
  AAPL           92.31               13            1.34              3.27        347.51                13.86         0.513            pass              0.514             38.3                           0.472                0.23              0.113                                 ok            True                  False
  FTNT           82.35               17            2.46              2.39        138.08                91.61         0.670            pass              0.258             27.3                           0.554              -19.77             -1.549            downtrend_blocked_slope           False                  False
  GOOG           76.92               13            1.67              3.29        280.91                50.42         0.643            pass              0.182             32.5                           0.535              -17.60             -1.776 downtrend_blocked_slope_and_streak           False                  False
 GOOGL           76.47               17            1.49              2.97        282.55                51.94         0.636            pass              0.226             38.6                           0.584              -17.91             -1.824 downtrend_blocked_slope_and_streak           False                  False
  ALNY           75.00                4            5.28              6.43        171.25               108.34         0.555            pass              0.098             14.2                           0.216              -28.90             -2.582            downtrend_blocked_slope           False                  False
  META           68.75               16            1.62              7.08        621.49                38.13         0.547            pass              0.197             34.2                           0.407              -13.38             -1.677 downtrend_blocked_slope_and_streak           False                  False
  MELI           68.18               22            1.91             22.14       1650.64                48.11         0.538            pass              0.244             36.9                           0.490              -11.21             -1.492 downtrend_blocked_slope_and_streak           False                  False
  ROST           73.33               15            1.51              2.46        231.25                24.69         0.505            pass              0.119             11.6                           0.232               -3.42             -0.407            downtrend_blocked_slope           False                  False
  ABNB           88.00               25            1.15              1.34        165.87                25.92         0.500 below_threshold              0.418             18.3                           0.299               -5.28             -0.688 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                            detail
2026-10-30T15:10:04.962037-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-10-30T15:05:04.984730-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-10-30T15:00:07.087528-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-10-30T14:55:05.117315-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-10-30T14:50:03.931152-04:00       entry_1500              entry {"allocated_cash": 58200.0, "asset_type": "option", "contract_symbol": "CEG261218C00260000", "contracts": 30, "early_entry_score": 0.369, "entry_mode": "regular", "entry_option_price": 19.4, "execution_mode": "option", "matched_signals": 25, "option_liquidity_status": "ok", "option_open_interest": 503.0, "option_spread_pct": 8.25, "option_volume": 30.0, "success_rate": 84.0, "ticker": "CEG", "timing_score": 0.589}
2026-10-30T14:50:03.931152-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                      {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-10-30", "training_samples": 6237, "window": 5}
2026-10-30T12:00:06.415858-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-30T11:55:05.950697-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-30T11:50:06.698728-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-30T11:45:05.073767-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261030155005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261030155005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261030155005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261030155005)

</details>
