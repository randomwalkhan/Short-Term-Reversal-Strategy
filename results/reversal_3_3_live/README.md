# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-03 15:25:05 EST`
Last processed slot: `manage_1530`

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

- Cash: `$68,296.55`
- Equity: `$134,096.55`
- Realized PnL: `$126,446.55`
- Unrealized PnL: `$-2,350.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  MDLZ     option         option MDLZ261218C00067500       2026-11-03                   0    470     68150.0                 65800.0         1.45            1.4       65.69         65.38          bid_ask_mid                        1.4                bid_ask_mid                    True         -2350.0                  -3.45         90.91               11              1.03         24.34            25.1                   28.2                1121.0           33.0               0.07                      ok
```

## Today's Closed Trades (2026-11-03)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
   CEG     option         option CEG261218C00260000     34          2026-11-02         2026-11-03        18.25       21.05 9520.0   15.342466 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
 CMCSA           92.31               13            1.03              0.17         23.80                32.70         0.597          pass              0.531             41.1                           0.360                5.66              0.525                                 ok            True                  False
   KHC           81.82               11            1.99              0.35         24.78                33.68         0.558          pass              0.175             21.4                           0.310                2.54              0.146                                 ok            True                  False
   ADP           86.96               23            0.71              1.49        298.14                27.85         0.535          pass              0.527             67.1                           0.500                1.33             -0.176                                 ok            True                  False
  FAST           96.30               27            0.51              0.19         52.47                22.62         0.514          pass              0.715             50.0                           0.329                1.73              0.090                                 ok            True                  False
   ROP           87.10               31            0.84              2.82        478.33                37.35         0.510          pass              0.577             65.5                           0.682               19.41              1.717                                 ok            True                  False
   XEL           86.36               22            0.67              0.37         79.17                19.18         0.506          pass              0.450             50.0                           0.316                2.76              0.289                                 ok            True                  False
  MDLZ           88.89                9            1.49              0.69         66.08                28.20         0.588          pass              0.379             27.7                           0.206                2.19              0.240                                 ok           False                  False
  MRVL           89.74               39            0.57              0.69        171.12                97.23         0.574          pass              0.737             75.6                           0.632              -29.11             -3.227 downtrend_blocked_slope_and_streak           False                  False
  TMUS           42.86                7            3.55              3.98        158.44                68.40         0.566          pass              0.063              2.0                           0.124               -2.08              0.028                                 ok           False                  False
   PEP           66.67                3            2.11              2.07        139.53                26.86         0.562          pass              0.062              2.0                           0.157                2.57              0.191                                 ok           False                  False
   EXC           66.67                3            1.69              0.55         46.21                22.18         0.554          pass              0.066              3.7                           0.176                6.12              0.689                                 ok           False                  False
 GOOGL           88.64               44            0.02              0.03        278.98                50.76         0.552          pass              0.782             98.8                           0.646              -18.03             -2.164 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-11-03T15:10:05.032509-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-11-03T15:05:04.979432-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-11-03T15:00:05.978517-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-11-03T14:55:04.978613-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-11-03T14:50:06.793337-05:00       entry_1500              entry {"allocated_cash": 68150.0, "asset_type": "option", "contract_symbol": "MDLZ261218C00067500", "contracts": 470, "early_entry_score": 0.508, "entry_mode": "regular", "entry_option_price": 1.45, "execution_mode": "option", "matched_signals": 11, "option_liquidity_status": "ok", "option_open_interest": 1121.0, "option_spread_pct": 6.9, "option_volume": 33.0, "success_rate": 90.91, "ticker": "MDLZ", "timing_score": 0.603}
2026-11-03T14:50:06.793337-05:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                          {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-11-03", "training_samples": 6256, "window": 5}
2026-11-03T12:00:06.009720-05:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-03T11:55:04.283382-05:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-03T11:50:06.620716-05:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-03T11:45:05.991467-05:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261103152505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261103152505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261103152505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261103152505)

</details>
