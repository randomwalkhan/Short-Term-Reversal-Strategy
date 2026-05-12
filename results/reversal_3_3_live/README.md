# Reversal 3.4.2 Live Paper Test

Latest checkpoint (ET): `2026-05-12 10:00:05 EDT`
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
- Equity: `$35,353.50`
- Realized PnL: `$25,353.50`
- Unrealized PnL: `$0.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SNPS     option         option SNPS260618C00520000       2026-05-12                   0      5     17500.0                 17500.0         35.0           35.0       510.5         510.5             0.0                    0.0         96.97               33               1.1          1.56            1.56                  42.97                 202.0           13.0                0.0                      ok
```

## Today's Closed Trades (2026-05-12)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  TEAM           85.71               35            1.84              1.13         86.83               115.89         0.688          pass              0.466             26.1                           0.333               22.94              2.522                  ok            True                  False
  INTC          100.00               10            4.50              4.08        127.69               104.15         0.621          pass              0.527             21.6                           0.279               46.25              3.931                  ok            True                  False
  FTNT           93.33               30            1.26              1.02        115.00                70.54         0.604          pass              0.569              6.5                           0.083               32.98              3.592                  ok            True                  False
  GOOG           87.50               32            0.79              2.14        385.85                39.86         0.558          pass              0.506             34.6                           0.322               10.42              1.044                  ok            True                  False
  MNST           80.00               20            1.35              0.82         86.06                49.64         0.555          pass              0.300             59.2                           0.305               10.44              1.174                  ok            True                  False
    ZS           80.77               26            1.68              1.75        148.12                59.15         0.548          pass              0.182              0.0                           0.150                7.57              1.244                  ok            True                  False
   XEL           92.86               14            1.14              0.64         80.32                27.14         0.539          pass              0.615             63.8                           0.369                0.25             -0.079                  ok            True                  False
  INTU           90.32               31            1.05              2.89        392.05                46.70         0.532          pass              0.589             40.1                           0.278               -2.80             -0.113                  ok            True                  False
  CDNS           96.30               27            1.67              4.27        362.37                37.36         0.518          pass              0.590              8.3                           0.127               10.08              1.152                  ok            True                  False
   CSX           86.67               30            0.74              0.23         44.64                30.07         0.514          pass              0.421             19.5                           0.215               -1.81             -0.122                  ok            True                  False
  ASML           85.71               14            3.54             38.85       1549.16                49.29         0.501          pass              0.245              5.2                           0.254                9.08              1.298                  ok            True                  False
   TXN           88.89                9            2.55              5.31        295.48                67.69         0.689          pass              0.338             10.6                           0.190               10.06              0.944                  ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                                                                                                                                                                                                                                                                           detail
2026-05-12T10:00:05.800159-04:00 early_entry_1000         entry {"allocated_cash": 17500.0, "asset_type": "option", "contract_symbol": "SNPS260618C00520000", "contracts": 5, "early_entry_score": 0.854, "entry_mode": "early", "entry_option_price": 35.0, "execution_mode": "option", "matched_signals": 33, "option_liquidity_status": "ok", "option_open_interest": 202.0, "option_spread_pct": 0.0, "option_volume": 13.0, "success_rate": 96.97, "ticker": "SNPS", "timing_score": 0.483}
2026-05-11T12:00:16.292660-04:00 early_entry_1200 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-11T11:53:58.426024-04:00 early_entry_1150 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-11T11:47:42.065930-04:00 early_entry_1145 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-11T11:41:24.132378-04:00 early_entry_1140 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-11T11:35:07.512033-04:00 early_entry_1135 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-11T11:28:46.452605-04:00 early_entry_1125 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-11T11:22:14.545933-04:00 early_entry_1120 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-11T11:15:52.009097-04:00 early_entry_1115 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-11T11:09:25.222860-04:00 early_entry_1105 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.2 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260512100005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.2 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260512100005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.2 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260512100005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.2 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260512100005)

</details>
