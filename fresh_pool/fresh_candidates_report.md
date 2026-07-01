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
1. `AKUN-001-UNKNOWN-VLESS-WS-67MS` (url=223ms, nekobox=253ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-65MS` (url=222ms, nekobox=250ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-84MS` (url=212ms, nekobox=235ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-72MS` (url=218ms, nekobox=241ms, status=yes)
5. `AKUN-005-COMPREND-NET-VLESS-WS-86MS` (url=199ms, nekobox=237ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-91MS` (url=225ms, nekobox=237ms, status=yes)
7. `AKUN-007-COMPREND-NET-VLESS-WS-92MS` (url=211ms, nekobox=230ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-71MS` (url=233ms, nekobox=231ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-86MS` (url=214ms, nekobox=253ms, status=yes)
10. `AKUN-010-COMPREND-NET-VLESS-WS-65MS` (url=204ms, nekobox=235ms, status=yes)
11. `AKUN-011-ZVC-VLESS-WS-83MS` (url=227ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-123MS` (url=215ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-86MS` (url=216ms, status=HTTP 204)
14. `AKUN-014-COMPREND-NET-VLESS-WS-89MS` (url=218ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-113MS` (url=209ms, status=HTTP 204)
16. `AKUN-016-COMPREND-NET-VLESS-WS-120MS` (url=235ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-145MS` (url=219ms, status=HTTP 204)
18. `AKUN-019-UNKNOWN-VLESS-WS-113MS` (url=213ms, status=HTTP 204)
19. `AKUN-021-UNKNOWN-VLESS-WS-235MS` (url=502ms, status=HTTP 204)
20. `AKUN-022-UNKNOWN-VLESS-WS-239MS` (url=508ms, status=HTTP 204)
21. `AKUN-023-UNKNOWN-VLESS-WS-109MS` (url=232ms, status=HTTP 204)
22. `AKUN-025-UNKNOWN-VLESS-WS-251MS` (url=562ms, status=HTTP 204)
23. `AKUN-026-CLOUDFLARE-VLESS-WS-253MS` (url=567ms, status=HTTP 204)
24. `AKUN-027-UNKNOWN-VLESS-WS-265MS` (url=546ms, status=HTTP 204)
25. `AKUN-028-UNKNOWN-VLESS-WS-256MS` (url=575ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
