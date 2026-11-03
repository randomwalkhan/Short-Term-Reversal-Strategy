# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-03 09:55:06 EST`
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
   CEG     option         option CEG261218C00260000       2026-11-02                   1     34     62050.0                 70210.0        18.25          20.65      257.89        263.77          bid_ask_mid                      20.65                bid_ask_mid                    True          8160.0                  13.15         85.19               27              1.71         52.01           50.56                  64.43                 487.0           31.0               0.03                      ok
```

## Today's Closed Trades (2026-11-03)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  IDXX           90.00               20            1.73              8.14        668.15                75.67         0.676          pass              0.485             27.9                           0.207               18.30              1.430                  ok            True                  False
 CMCSA           91.67               12            1.17              0.20         23.79                32.70         0.594          pass              0.482             32.7                           0.291                5.50              0.518                  ok            True                  False
  CTAS           94.44               18            1.13              1.77        224.01                26.23         0.543          pass              0.591             32.6                           0.282                2.40              0.028                  ok            True                  False
   XEL           81.82               11            1.16              0.64         79.05                19.18         0.540          pass              0.151             14.0                           0.185                2.26              0.267                  ok            True                  False
    ZS           91.67               36            0.74              1.17        223.29                66.63         0.537          pass              0.704             55.2                           0.401                3.55             -0.031                  ok            True                  False
   EXC           81.25               16            0.95              0.31         46.32                22.18         0.536          pass              0.221             31.2                           0.393                6.93              0.724                  ok            True                  False
  INSM           82.61               46            0.59              0.45        109.12                58.20         0.504          pass              0.421             33.7                           0.249               13.58              1.946                  ok            True                  False
  TMUS           55.56                9            2.28              2.56        159.06                68.40         0.648          pass              0.115             16.9                           0.204               -0.79              0.088                  ok           False                  False
   PEP           83.33                6            1.56              1.53        139.76                26.86         0.593          pass              0.209             20.3                           0.245                3.15              0.217                  ok           False                  False
  MDLZ           66.67                3            1.84              0.85         66.01                28.20         0.581          pass              0.091             10.9                           0.157                1.83              0.224                  ok           False                  False
   KHC           83.33                6            2.15              0.37         24.77                33.68         0.580          pass              0.192             15.1                           0.196                2.37              0.139                  ok           False                  False
   ROP           70.00               10            1.70              5.69        477.10                37.35         0.572          pass              0.148             30.3                           0.405               18.38              1.677                  ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-11-03T00:00:06.091042-05:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                           {'saved': 91, 'empty': 2}
2026-11-02T15:10:04.822162-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-11-02T15:05:06.352149-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-11-02T15:00:04.459159-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-11-02T14:55:05.914374-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-11-02T14:50:01.614756-05:00       entry_1500              entry {"allocated_cash": 62050.0, "asset_type": "option", "contract_symbol": "CEG261218C00260000", "contracts": 34, "early_entry_score": 0.324, "entry_mode": "regular", "entry_option_price": 18.25, "execution_mode": "option", "matched_signals": 27, "option_liquidity_status": "ok", "option_open_interest": 487.0, "option_spread_pct": 2.74, "option_volume": 31.0, "success_rate": 85.19, "ticker": "CEG", "timing_score": 0.582}
2026-11-02T14:50:01.614756-05:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                        {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-11-02", "training_samples": 6238, "window": 5}
2026-11-02T12:00:05.602652-05:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-02T11:55:05.694334-05:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-02T11:50:03.622445-05:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261103095506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261103095506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261103095506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261103095506)

</details>
