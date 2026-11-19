# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-19 10:15:01 EST`
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

- Cash: `$56,193.80`
- Equity: `$100,818.80`
- Realized PnL: `$95,918.80`
- Unrealized PnL: `$-5,100.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   APP     option         option APP270115C00400000       2026-11-18                   1     15     49725.0                 44625.0        33.15          29.75      389.81         384.2          bid_ask_mid                      29.75                bid_ask_mid                    True         -5100.0                 -10.26         90.91               22              2.29         60.57           59.33                 121.47                4183.0           24.0               0.06                      ok
```

## Today's Closed Trades (2026-11-19)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
   APP           90.91               33            1.58              4.31        389.06               121.61         0.763          pass              0.651             43.4                           0.293                8.05              0.372                  ok            True                  False
  IDXX           95.65               23            1.41              6.91        695.51                78.12         0.727          pass              0.593             11.3                           0.116                2.67              0.187                  ok            True                  False
  ABNB           86.21               29            1.13              1.43        179.60                55.20         0.570          pass              0.408             19.5                           0.209                4.73             -0.099                  ok            True                  False
  REGN           80.00               30            1.11              7.37        942.37                54.27         0.567          pass              0.343             51.0                           0.384                3.56              0.498                  ok            True                  False
 CMCSA           92.31               13            1.70              0.30         25.11                34.19         0.563          pass              0.434              9.9                           0.192               -0.55              0.253                  ok            True                  False
  AAPL          100.00               20            0.91              2.24        351.49                27.20         0.557          pass              0.582             19.8                           0.248                1.55              0.216                  ok            True                  False
  FAST           90.00               10            1.19              0.45         53.77                20.11         0.556          pass              0.340              5.9                           0.230                0.79              0.095                  ok            True                  False
  COST           88.89               18            0.87              6.71       1093.74                23.52         0.551          pass              0.417             24.0                           0.268                2.01              0.441                  ok            True                  False
  ODFL           85.71               28            1.07              1.31        174.55                43.99         0.548          pass              0.327              0.0                           0.150                1.57              0.392                  ok            True                  False
   CEG           92.11               38            0.62              1.15        262.25                59.92         0.532          pass              0.563              0.0                           0.150                9.12              0.595                  ok            True                  False
   HON           80.00               25            0.84              1.31        222.14                33.05         0.526          pass              0.153              0.0                           0.189                2.66             -0.035                  ok            True                  False
   CSX           82.35               17            1.29              0.46         51.13                35.07         0.524          pass              0.187              8.3                           0.165               -0.31              0.217                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-11-19T10:15:01.694448-05:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-19T10:10:05.743746-05:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-19T10:05:05.527736-05:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-19T10:00:06.381004-05:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-19T00:00:05.435730-05:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                            {'saved': 91, 'empty': 2}
2026-11-18T15:10:05.947802-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-11-18T15:05:06.246695-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-11-18T15:00:06.306059-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-11-18T14:55:05.603926-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-11-18T14:50:05.341851-05:00       entry_1500              entry {"allocated_cash": 49725.0, "asset_type": "option", "contract_symbol": "APP270115C00400000", "contracts": 15, "early_entry_score": 0.497, "entry_mode": "regular", "entry_option_price": 33.15, "execution_mode": "option", "matched_signals": 22, "option_liquidity_status": "ok", "option_open_interest": 4183.0, "option_spread_pct": 5.73, "option_volume": 24.0, "success_rate": 90.91, "ticker": "APP", "timing_score": 0.787}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261119101501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261119101501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261119101501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261119101501)

</details>
