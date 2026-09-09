# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-09 10:10:05 EDT`
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

- Cash: `$39,968.10`
- Equity: `$77,733.10`
- Realized PnL: `$67,148.10`
- Unrealized PnL: `$585.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CRWD     option         option CRWD261016C00210000       2026-09-08                   1     26     37180.0                 37765.0         14.3          14.52      209.63        209.33          bid_ask_mid                      14.52                bid_ask_mid                    True           585.0                   1.57         88.89               36              1.63         52.75           54.54                  91.63                 699.0          116.0               0.04                      ok
```

## Today's Closed Trades (2026-09-09)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   PEP           87.50               16            0.57              0.55        138.21                16.46         0.546          pass              0.407             37.3                           0.468               -2.21             -0.184                                 ok            True                  False
  NVDA           91.18               34            0.62              0.99        225.31                44.12         0.541          pass              0.586             24.5                           0.221                5.29              0.635                                 ok            True                  False
  LRCX           82.93               41            0.52              1.16        319.92                52.73         0.513          pass              0.552             74.2                           0.619                1.30             -0.047                                 ok            True                  False
  CPRT           80.00               25            1.52              0.35         32.45                44.55         0.509          pass              0.278             42.4                           0.510               -3.68             -0.090                                 ok            True                  False
  TMUS           91.67               12            1.66              2.11        180.79                25.45         0.504          pass              0.408             11.2                           0.169               -1.05              0.187                                 ok            True                  False
  MSFT           89.29               28            0.64              2.23        493.00                23.28         0.501          pass              0.424              2.1                           0.047               -0.19             -0.087                                 ok            True                  False
  MSTR           85.00               40            0.22              0.21        136.43               103.38         0.717          pass              0.492             29.1                           0.145                7.40              0.968                                 ok           False                  False
  CRWD           91.30               46            0.30              0.45        209.83                89.86         0.661          pass              0.741             57.9                           0.342               12.95              0.605                                 ok           False                  False
  WDAY           92.50               40            0.41              0.54        186.05                77.37         0.623          pass              0.811             71.8                           0.552               -4.58             -0.233                                 ok           False                  False
   KHC          100.00               13            0.42              0.07         24.87                28.58         0.623          pass              0.684             67.2                           0.669               -0.51              0.064                                 ok           False                  False
  PYPL           94.74               38            0.17              0.06         53.15                58.35         0.588          pass              0.922             94.4                           0.787              -14.53             -1.412 downtrend_blocked_slope_and_streak           False                  False
  PAYX          100.00               20            0.94              0.77        116.60                30.90         0.561          pass              0.646             41.1                           0.392               -7.33             -0.742            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-09-09T10:10:05.084916-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-09T10:05:03.958272-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-09T10:00:05.981446-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-09T00:00:04.345374-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                        {'saved': 93}
2026-09-08T15:10:02.485838-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-09-08T15:05:04.629730-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-09-08T15:00:03.621763-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-09-08T14:55:03.619621-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-09-08T14:50:01.652709-04:00       entry_1500              entry {"allocated_cash": 37180.0, "asset_type": "option", "contract_symbol": "CRWD261016C00210000", "contracts": 26, "early_entry_score": 0.637, "entry_mode": "regular", "entry_option_price": 14.3, "execution_mode": "option", "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 699.0, "option_spread_pct": 4.2, "option_volume": 116.0, "success_rate": 88.89, "ticker": "CRWD", "timing_score": 0.617}
2026-09-08T14:50:01.652709-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                         {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-09-08", "training_samples": 5748, "window": 5}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260909101005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260909101005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260909101005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260909101005)

</details>
