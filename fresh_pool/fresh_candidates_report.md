# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 22
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 28

## Cara Pakai di OpenWrt
Jalankan manual saat node mulai mati:

```sh
sh /etc/mihomo-autopilot/openwrt_pull_fresh_pool.sh
```

Atau aktifkan guard otomatis:

```sh
sh /etc/mihomo-autopilot/openwrt_fresh_guard.sh
```

## Kandidat Fresh Teratas
1. `AKUN-001-090227-VLESS-WS-58MS` (url=211ms, nekobox=248ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-85MS` (url=221ms, nekobox=236ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-80MS` (url=237ms, nekobox=253ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-87MS` (url=204ms, nekobox=268ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-82MS` (url=214ms, nekobox=239ms, status=yes)
6. `AKUN-006-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-125MS` (url=238ms, nekobox=252ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-136MS` (url=222ms, nekobox=205ms, status=no)
8. `AKUN-008-DEV-VLESS-WS-81MS` (url=244ms, nekobox=197ms, status=no)
9. `AKUN-009-DEV-VLESS-WS-93MS` (url=229ms, nekobox=190ms, status=no)
10. `AKUN-010-DEV-VLESS-WS-142MS` (url=245ms, nekobox=188ms, status=no)
11. `AKUN-007-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-86MS`
12. `AKUN-008-RS-RAPIDSEEDBOX-20190717-VLESS-WS-94MS`
13. `AKUN-009-CLOUDFLARE-VLESS-WS-393MS`
14. `AKUN-010-CONFLU-VLESS-WS-395MS`
15. `AKUN-016-CLOUDFLARE-VLESS-WS-402MS` (url=796ms, status=HTTP 204)
16. `AKUN-018-CLOUDFLARE-VLESS-WS-423MS` (url=859ms, status=HTTP 204)
17. `AKUN-019-CLOUDFLARE-VLESS-WS-512MS` (url=923ms, status=HTTP 204)
18. `AKUN-024-CLOUDFLARE-VLESS-WS-640MS` (url=871ms, status=HTTP 204)
19. `AKUN-027-BIGCOMMERCE-VLESS-WS-669MS` (url=1223ms, status=HTTP 204)
20. `AKUN-032-CLOUDFLARE-VLESS-WS-705MS` (url=645ms, status=HTTP 204)
21. `AKUN-033-UNKNOWN-VLESS-WS-775MS` (url=1221ms, status=HTTP 204)
22. `AKUN-035-SRTONGSTON-VLESS-WS-769MS` (url=1034ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
