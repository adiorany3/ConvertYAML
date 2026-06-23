# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 25
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 31

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
1. `AKUN-001-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-63MS` (url=217ms, nekobox=230ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-70MS` (url=231ms, nekobox=244ms, status=yes)
3. `AKUN-003-NET-NL-VLESS-WS-74MS` (url=205ms, nekobox=238ms, status=yes)
4. `AKUN-004-NETCUP-VLESS-WS-76MS` (url=203ms, nekobox=239ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-69MS` (url=227ms, nekobox=189ms, status=no)
6. `AKUN-005-DIGITALOCEAN-VLESS-WS-70MS`
7. `AKUN-006-UNKNOWN-VLESS-WS-80MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-69MS`
9. `AKUN-010-CLOUDFLARE-VLESS-WS-79MS` (url=228ms, nekobox=205ms, status=no)
10. `AKUN-008-UNKNOWN-VLESS-WS-87MS`
11. `AKUN-009-UNKNOWN-VLESS-WS-86MS`
12. `AKUN-010-CLOUDFLARE-VLESS-WS-77MS`
13. `AKUN-014-UNKNOWN-VLESS-WS-83MS` (url=222ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-71MS` (url=211ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-82MS` (url=229ms, status=HTTP 204)
16. `AKUN-017-RS-RAPIDSEEDBOX-20190717-VLESS-WS-105MS` (url=227ms, status=HTTP 204)
17. `AKUN-018-UNKNOWN-VLESS-WS-81MS` (url=220ms, status=HTTP 204)
18. `AKUN-019-RS-RAPIDSEEDBOX-20190717-VLESS-WS-117MS` (url=213ms, status=HTTP 204)
19. `AKUN-020-US-VLESS-WS-126MS` (url=228ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-113MS` (url=245ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-70MS` (url=223ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-251MS` (url=560ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-239MS` (url=493ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-227MS` (url=502ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-243MS` (url=488ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
