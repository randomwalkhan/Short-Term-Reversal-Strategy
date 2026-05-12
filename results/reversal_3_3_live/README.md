# Reversal 3.4.2 Live Paper Test

Latest checkpoint (ET): `2026-05-12 10:10:05 EDT`
Last processed slot: `manage_1000`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Early-entry permission: `10:00 AM-12:00 PM ET` 5-minute scans may enter one exceptional candidate only when `early_entry_score >= 0.67`, success rate `>= 88%`, matched signals `>= 30`, early reclaim `>= 60%`, and recovery stability `>= 0.55`; the one-new-entry-per-day limit still applies
- Exit scans: `9:30 AM ET` and every `30` minutes through `4:00 PM ET`; off-hours `5-minute` checkpoints continue mark-to-market updates for open positions, while any legacy share positions still held from older versions continue extended-hours take-profit and stop loss scans until flat
- Live exit ladder: `+15% / +15% / -10%`
- Option entry liquidity gate: `open interest >= 100`, `volume >= 10`, `spread <= 15%`
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- Trend-health gate: block candidates in a short-term down channel when 10d return <= `-1.5%` and either log-slope <= `-0.25%/day` below the 10d lookback average or lower-close streak >= `4`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries use the current option mark price; regular-session stop-loss exits book the planned stop level, with no intraday future path otherwise assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$17,853.50`
- Equity: `$33,778.50`
- Realized PnL: `$25,353.50`
- Unrealized PnL: `$-1,575.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SNPS     option         option SNPS260618C00520000       2026-05-12                   0      5     17500.0                 15925.0         35.0          31.85       510.5         513.7         -1575.0                   -9.0         96.97               33               1.1          1.56           52.34                  42.97                 202.0           13.0                0.0                      ok
```

## Today's Closed Trades (2026-05-12)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  TEAM           87.50               40            1.01              0.62         87.05               115.89         0.706          pass              0.649             59.6                           0.377               23.99              2.560                  ok            True                  False
   TXN           91.67               12            2.14              4.46        295.85                67.69         0.696          pass              0.469             24.9                           0.270               10.52              0.963                  ok            True                  False
  INTC          100.00               10            4.45              4.03        127.71               104.15         0.623          pass              0.530             22.6                           0.217               46.33              3.933                  ok            True                  False
  FTNT           93.94               33            0.91              0.74        115.12                70.54         0.604          pass              0.708             41.0                           0.287               33.45              3.608                  ok            True                  False
  GOOG           84.62               26            1.10              2.99        385.49                39.86         0.573          pass              0.313              8.8                           0.155               10.07              1.030                  ok            True                  False
  SBUX           95.45               22            1.22              0.91        105.35                32.96         0.546          pass              0.661             42.2                           0.301                7.37              0.303                  ok            True                  False
   XEL           91.67               12            1.25              0.70         80.30                27.14         0.543          pass              0.560             60.4                           0.389                0.14             -0.084                  ok            True                  False
    ZS           83.33               36            0.87              0.91        148.48                59.15         0.536          pass              0.471             51.9                           0.357                8.45              1.281                  ok            True                  False
  ASML           87.50               16            3.00             32.85       1551.73                49.29         0.520          pass              0.351             19.8                           0.281                9.70              1.323                  ok            True                  False
  CDNS           96.55               29            1.43              3.65        362.64                37.36         0.518          pass              0.657             26.3                           0.273               10.35              1.164                  ok            True                  False
  INTU           88.57               35            0.93              2.56        392.19                46.70         0.512          pass              0.587             47.0                           0.413               -2.68             -0.108                  ok            True                  False
   CSX           86.21               29            0.85              0.27         44.63                30.07         0.510          pass              0.411             22.4                           0.215               -1.92             -0.128                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                                                                                                                                                                                                                                                                           detail
2026-05-12T10:10:05.279382-04:00 early_entry_1010 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-12T10:05:06.121865-04:00 early_entry_1005 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-12T10:00:05.800159-04:00 early_entry_1000         entry {"allocated_cash": 17500.0, "asset_type": "option", "contract_symbol": "SNPS260618C00520000", "contracts": 5, "early_entry_score": 0.854, "entry_mode": "early", "entry_option_price": 35.0, "execution_mode": "option", "matched_signals": 33, "option_liquidity_status": "ok", "option_open_interest": 202.0, "option_spread_pct": 0.0, "option_volume": 13.0, "success_rate": 96.97, "ticker": "SNPS", "timing_score": 0.483}
2026-05-11T12:00:16.292660-04:00 early_entry_1200 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-11T11:53:58.426024-04:00 early_entry_1150 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-11T11:47:42.065930-04:00 early_entry_1145 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-11T11:41:24.132378-04:00 early_entry_1140 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-11T11:35:07.512033-04:00 early_entry_1135 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-11T11:28:46.452605-04:00 early_entry_1125 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-11T11:22:14.545933-04:00 early_entry_1120 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.2 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260512101005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.2 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260512101005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.2 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260512101005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.2 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260512101005)

</details>
