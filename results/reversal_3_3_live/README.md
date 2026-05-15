# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-15 09:40:04 EDT`
Last processed slot: `manage_0930`

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
- Option entry liquidity gate: `open interest >= 110`, `volume >= 20`, `spread <= 14%`
- Option exit safety: stale option `lastPrice` may be shown for mark-to-market, but take-profit / stop-loss triggers require an executable quote from bid/ask or bid
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- Trend-health gate: block candidates in a short-term down channel when 10d return <= `-1.5%` and either log-slope <= `-0.25%/day` below the 10d lookback average or lower-close streak >= `4`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries use the current option mark price; regular-session stop-loss exits book the planned stop level, with no intraday future path otherwise assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$4,018.50`
- Equity: `$34,003.50`
- Realized PnL: `$23,603.50`
- Unrealized PnL: `$400.00`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SNPS     option         option SNPS260618C00490000       2026-05-13                   2      3     13410.0                 13785.0        44.70          45.95      510.62        505.25     last_price_stale                        NaN                unavailable                   False           375.0                   2.80         97.14               35              0.50         52.16             0.0                  43.23                 154.0           10.0               0.12                      ok
  CDNS     option         option CDNS260618C00330000       2026-05-14                   1      5     16175.0                 16200.0        32.35          32.40      352.55        349.81     last_price_stale                        NaN                unavailable                   False            25.0                   0.15         97.30               37              0.56         47.46             0.0                  37.69                2023.0           40.0               0.10                      ok
```

## Today's Closed Trades (2026-05-15)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
   TXN           88.24               17            1.52              3.28        306.76                67.99         0.702          pass              0.511             58.0                           0.794                8.54              1.038                      ok            True                  False
  FTNT           96.88               32            0.94              0.81        121.51                71.29         0.625          pass              0.825             71.9                           0.428               39.89              3.882                      ok            True                  False
  GOOG           82.35               17            1.50              4.16        395.39                40.76         0.588          pass              0.246             25.8                           0.385                2.09              0.288                      ok            True                  False
 GOOGL           81.25               16            1.56              4.37        399.20                40.65         0.587          pass              0.214             27.2                           0.448                2.37              0.298                      ok            True                  False
  SNPS           97.14               35            0.94              3.34        508.59                41.57         0.535          pass              0.777             52.4                           0.540                3.32              0.326                      ok            True                  False
   HON           80.00               10            1.98              3.02        216.42                27.08         0.533          pass              0.068              5.1                           0.131                0.42              0.298                      ok            True                  False
  CDNS           96.77               31            1.17              2.90        351.60                37.94         0.527          pass              0.717             41.4                           0.420                2.28              0.178                      ok            True                  False
   CSX           81.82               22            1.08              0.35         45.77                31.64         0.509          pass              0.313             44.4                           0.319                0.74              0.054                      ok            True                  False
  SBUX           97.06               34            0.71              0.53        106.17                33.04         0.507          pass              0.748             45.7                           0.535               -0.25              0.079                      ok            True                  False
  MPWR           83.33               18            2.61             29.50       1601.33                52.07         0.507          pass              0.292             32.9                           0.530               -0.74              0.153                      ok            True                  False
  CHTR           80.95               21            2.15              2.23        147.05               114.29         0.754          pass              0.190              5.4                           0.156              -15.67             -1.629 downtrend_blocked_slope           False                  False
  NXPI           76.19               21            2.01              4.15        292.39                90.16         0.720          pass              0.256             36.9                           0.507               -2.37             -0.019                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                                                                                                                                                                                                                                                                                                                                            detail
2026-05-15T00:00:05.036344-04:00     data_refresh   data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                     {'saved': 92}
2026-05-14T15:10:04.841035-04:00       entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-05-14T15:05:08.308131-04:00       entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-05-14T15:00:08.187447-04:00       entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-05-14T14:55:08.383255-04:00       entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-05-14T14:50:07.158439-04:00       entry_1500  entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "daily_entry_limit"}
2026-05-14T14:50:07.158439-04:00       entry_1500 timing_overlay                                                                                                                                                                                                                                                                                                                      {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-05-14", "training_samples": 5049, "window": 5}
2026-05-14T11:37:47.828844-04:00 early_entry_1135  entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "daily_entry_limit"}
2026-05-14T10:50:02.088724-04:00 early_entry_1050  entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "daily_entry_limit"}
2026-05-14T10:06:24.763261-04:00 early_entry_1005          entry {"allocated_cash": 16175.0, "asset_type": "option", "contract_symbol": "CDNS260618C00330000", "contracts": 5, "early_entry_score": 0.833, "entry_mode": "early", "entry_option_price": 32.35, "execution_mode": "option", "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 2023.0, "option_spread_pct": 10.2, "option_volume": 40.0, "success_rate": 97.3, "ticker": "CDNS", "timing_score": 0.51}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260515094004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260515094004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260515094004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260515094004)

</details>
