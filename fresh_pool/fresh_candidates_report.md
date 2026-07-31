# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 23
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 27

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
1. `AKUN-001-UNKNOWN-VLESS-WS-55MS` (url=218ms, nekobox=236ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-58MS` (url=219ms, nekobox=225ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-56MS` (url=224ms, nekobox=235ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-59MS` (url=213ms, nekobox=239ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-59MS` (url=208ms, nekobox=248ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-57MS` (url=200ms, nekobox=234ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-64MS` (url=221ms, nekobox=237ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-80MS` (url=221ms, nekobox=235ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-71MS` (url=211ms, nekobox=239ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-86MS` (url=221ms, nekobox=250ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-103MS` (url=217ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-61MS` (url=212ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-132MS` (url=201ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-167MS` (url=214ms, status=HTTP 204)
15. `AKUN-017-CLOUDFLARE-VLESS-WS-229MS` (url=656ms, status=HTTP 204)
16. `AKUN-019-090227-VLESS-WS-299MS` (url=622ms, status=HTTP 204)
17. `AKUN-022-CLOUDFLARE-VLESS-WS-323MS` (url=1174ms, status=HTTP 204)
18. `AKUN-026-SUKARIO-VLESS-WS-593MS` (url=985ms, status=HTTP 204)
19. `AKUN-027-UNKNOWN-VLESS-WS-622MS` (url=964ms, status=HTTP 204)
20. `AKUN-029-CLOUDFLARE-VLESS-WS-661MS` (url=1107ms, status=HTTP 204)
21. `AKUN-031-CLOUDFLARE-VLESS-WS-704MS` (url=1186ms, status=HTTP 204)
22. `AKUN-033-UNKNOWN-VLESS-WS-757MS` (url=1290ms, status=HTTP 204)
23. `AKUN-035-UNKNOWN-VLESS-WS-721MS` (url=1123ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
