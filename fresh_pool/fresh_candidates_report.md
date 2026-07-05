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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-77MS` (url=218ms, nekobox=249ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-77MS` (url=228ms, nekobox=254ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-84MS` (url=211ms, nekobox=204ms, status=no)
4. `AKUN-003-CLOUDFLARE-VLESS-WS-81MS`
5. `AKUN-004-ZVC-VLESS-WS-89MS`
6. `AKUN-005-OVH-VLESS-WS-89MS`
7. `AKUN-006-ZVC-VLESS-WS-96MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-95MS`
9. `AKUN-008-UNKNOWN-VLESS-WS-108MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-88MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-99MS`
12. `AKUN-012-TENCENT-VLESS-WS-94MS` (url=208ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-108MS` (url=224ms, status=HTTP 204)
14. `AKUN-014-466688-VLESS-WS-131MS` (url=204ms, status=HTTP 204)
15. `AKUN-016-WPENG-VLESS-WS-121MS` (url=221ms, status=HTTP 204)
16. `AKUN-017-WPENG-VLESS-WS-130MS` (url=230ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-107MS` (url=214ms, status=HTTP 204)
18. `AKUN-019-WEYRO-NET-VLESS-WS-169MS` (url=211ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-136MS` (url=234ms, status=HTTP 204)
20. `AKUN-021-CONFLU-VLESS-WS-250MS` (url=501ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-239MS` (url=511ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-249MS` (url=567ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-243MS` (url=520ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-262MS` (url=552ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-266MS` (url=558ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
