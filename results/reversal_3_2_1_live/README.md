# Reversal 3.2.2 Live Paper Test

Latest checkpoint (ET): `2026-04-15 15:15:05 EDT`
Last processed slot: `manual`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Exit scans: `9:30 AM ET` and every `30` minutes through `4:00 PM ET`; off-hours `5-minute` checkpoints continue mark-to-market updates for open positions, while share-fallback positions also run take-profit and stop loss scans in after-hours / overnight / pre-market
- Live exit ladder: `+15% / +15% / -12%`
- Option entry liquidity gate: `open interest >= 100`, `volume >= 10`, `spread <= 15%`
- Fallback execution: buy shares when the option fails the liquidity gate; use `+3% / -3%` for common-stock fallback and `+5% / -5%` for leveraged-ETF shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; share positions can additionally trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries and exits use the current option mark price; no intraday future path is assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$1,294.00`
- Equity: `$14,314.76`
- Realized PnL: `$4,230.00`
- Unrealized PnL: `$84.76`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct      option_liquidity_status
  REGN      share share_fallback               REGN       2026-04-13                   2      8      5916.0                 6000.76        739.5         750.09      739.50        750.09           84.76                   1.43         100.0               24              1.25           NaN             NaN                  24.22                  89.0            1.0               0.07 low_open_interest,low_volume
   HON     option         option HON260515C00240000       2026-04-15                   0     18      7020.0                 7020.00          3.9           3.90      231.34        231.66            0.00                   0.00         100.0               22              0.82         27.49           27.54                  23.78                2322.0          110.0               0.05                           ok
```

## Today's Closed Trades (2026-04-15)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  FANG     option         option FANG260515C00185000      7          2026-04-14         2026-04-15          8.8       10.35 1085.0   17.613636 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  REGN          100.00               33            0.72              3.79        753.89                24.04            True
   HON          100.00               24            0.64              1.05        232.79                23.78            True
   AEP           94.12               17            0.80              0.75        135.14                19.01            True
   STX           92.59               27            2.69             10.06        529.13                74.84            True
  ALNY           92.11               38            1.09              2.59        338.30                42.77            True
  GILD           90.32               31            0.52              0.51        140.23                21.91            True
  MPWR           90.00               30            1.70             16.19       1356.48                58.76            True
   MAR           89.19               37            0.61              1.56        366.03                29.18            True
   EXC           88.24               17            0.84              0.29         48.49                21.52            True
   CSX           86.36               22            0.95              0.28         42.39                21.52            True
  SOXL           84.85               33            1.75              1.04         84.86               129.42            True
  KLAC           84.62               13            4.01             50.37       1774.32                50.02            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                                                                                                                                                                                                                                 detail
2026-04-15T15:10:01.074432-04:00  entry_1500 slot_skipped                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-04-15T15:05:05.906794-04:00  entry_1500 slot_skipped                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-04-15T15:00:05.949066-04:00  entry_1500 slot_skipped                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-04-15T14:55:00.892312-04:00  entry_1500 slot_skipped                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-04-15T14:50:03.896088-04:00  entry_1500        entry {"allocated_cash": 7020.0, "asset_type": "option", "contract_symbol": "HON260515C00240000", "contracts": 18, "entry_option_price": 3.9, "execution_mode": "option", "matched_signals": 22, "option_liquidity_status": "ok", "option_open_interest": 2322.0, "option_spread_pct": 5.13, "option_volume": 110.0, "success_rate": 100.0, "ticker": "HON"}
2026-04-15T14:40:01.721975-04:00 manage_1430 slot_skipped                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-04-15T14:35:00.735526-04:00 manage_1430 slot_skipped                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-04-15T14:30:01.739266-04:00 manage_1430 slot_skipped                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-04-15T14:25:01.819991-04:00 manage_1430 slot_skipped                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-04-15T14:10:00.708048-04:00 manage_1400 slot_skipped                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.2 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260415151505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.2 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260415151505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.2 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260415151505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.2 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260415151505)

</details>
