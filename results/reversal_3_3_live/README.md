# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-03 10:00:06 EST`
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

- Cash: `$64,876.55`
- Equity: `$135,086.55`
- Realized PnL: `$116,926.55`
- Unrealized PnL: `$8,160.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   CEG     option         option CEG261218C00260000       2026-11-02                   1     34     62050.0                 70210.0        18.25          20.65      257.89        262.98          bid_ask_mid                      20.65                bid_ask_mid                    True          8160.0                  13.15         85.19               27              1.71         52.01           51.29                  64.43                 487.0           31.0               0.03                      ok
```

## Today's Closed Trades (2026-11-03)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  IDXX           90.00               20            1.64              7.71        668.34                75.67         0.681          pass              0.497             31.7                           0.233               18.41              1.434                                 ok            True                  False
 CMCSA           91.67               12            1.15              0.19         23.79                32.70         0.595          pass              0.486             33.9                           0.280                5.52              0.519                                 ok            True                  False
   PEP           81.82               11            1.45              1.42        139.81                26.86         0.568          pass              0.189             25.7                           0.295                3.26              0.222                                 ok            True                  False
   KHC           80.00               10            2.09              0.36         24.77                33.68         0.556          pass              0.108             17.5                           0.205                2.43              0.142                                 ok            True                  False
  CTAS           95.24               21            0.90              1.42        224.16                26.23         0.539          pass              0.665             45.9                           0.348                2.63              0.038                                 ok            True                  False
    ZS           91.18               34            1.18              1.85        223.00                66.63         0.523          pass              0.597             29.0                           0.255                3.10             -0.051                                 ok            True                  False
   XEL           80.00               15            1.01              0.56         79.09                19.18         0.522          pass              0.160             24.8                           0.283                2.41              0.273                                 ok            True                  False
   EXC           85.71               21            0.85              0.28         46.33                22.18         0.515          pass              0.392             38.3                           0.470                7.03              0.728                                 ok            True                  False
  TMUS           63.64               11            1.83              2.05        159.27                68.40         0.669          pass              0.173             33.3                           0.288               -0.34              0.109                                 ok           False                  False
  MDLZ           83.33                6            1.58              0.73         66.07                28.20         0.595          pass              0.218             23.4                           0.271                2.09              0.236                                 ok           False                  False
  MRVL           90.24               41            0.23              0.27        171.29                97.23         0.594          pass              0.782             83.2                           0.368              -28.87             -3.212 downtrend_blocked_slope_and_streak           False                  False
   ROP           70.00               10            1.79              6.01        476.96                37.35         0.567          pass              0.136             26.4                           0.441               18.27              1.673                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-11-03T10:00:06.027735-05:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-03T00:00:06.091042-05:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                           {'saved': 91, 'empty': 2}
2026-11-02T15:10:04.822162-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-11-02T15:05:06.352149-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-11-02T15:00:04.459159-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-11-02T14:55:05.914374-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-11-02T14:50:01.614756-05:00       entry_1500              entry {"allocated_cash": 62050.0, "asset_type": "option", "contract_symbol": "CEG261218C00260000", "contracts": 34, "early_entry_score": 0.324, "entry_mode": "regular", "entry_option_price": 18.25, "execution_mode": "option", "matched_signals": 27, "option_liquidity_status": "ok", "option_open_interest": 487.0, "option_spread_pct": 2.74, "option_volume": 31.0, "success_rate": 85.19, "ticker": "CEG", "timing_score": 0.582}
2026-11-02T14:50:01.614756-05:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                        {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-11-02", "training_samples": 6238, "window": 5}
2026-11-02T12:00:05.602652-05:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-02T11:55:05.694334-05:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261103100006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261103100006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261103100006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261103100006)

</details>
