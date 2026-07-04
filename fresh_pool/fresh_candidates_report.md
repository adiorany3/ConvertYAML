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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-98MS` (url=283ms, nekobox=304ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-104MS` (url=293ms, nekobox=289ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-119MS` (url=276ms, nekobox=291ms, status=yes)
4. `AKUN-004-ZVC-VLESS-WS-107MS` (url=527ms, nekobox=306ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-115MS` (url=278ms, nekobox=287ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-115MS` (url=242ms, nekobox=310ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-125MS` (url=273ms, nekobox=310ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-131MS` (url=243ms, nekobox=279ms, status=yes)
9. `AKUN-009-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-126MS` (url=256ms, nekobox=332ms, status=yes)
10. `AKUN-010-ZVC-VLESS-WS-130MS` (url=273ms, nekobox=278ms, status=yes)
11. `AKUN-011-WEYRO-NET-VLESS-WS-136MS` (url=293ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-142MS` (url=289ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-114MS` (url=277ms, status=HTTP 204)
14. `AKUN-014-WPENG-VLESS-WS-151MS` (url=238ms, status=HTTP 204)
15. `AKUN-015-AEZA-NETWORK-VLESS-WS-132MS` (url=264ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-139MS` (url=264ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-99MS` (url=289ms, status=HTTP 204)
18. `AKUN-018-466688-VLESS-WS-144MS` (url=259ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-131MS` (url=276ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-167MS` (url=326ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-294MS` (url=720ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-302MS` (url=612ms, status=HTTP 204)
23. `AKUN-023-GUARDNETWORK-VLESS-WS-320MS` (url=743ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-317MS` (url=770ms, status=HTTP 204)
25. `AKUN-025-RS-RAPIDSEEDBOX-20190717-VLESS-WS-310MS` (url=653ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
