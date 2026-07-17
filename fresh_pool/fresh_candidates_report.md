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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-89MS` (url=232ms, nekobox=242ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-91MS` (url=251ms, nekobox=259ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-88MS` (url=225ms, nekobox=249ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-90MS` (url=224ms, nekobox=276ms, status=yes)
5. `AKUN-005-GO-DADDY-COM-LLC-VLESS-WS-99MS` (url=218ms, nekobox=266ms, status=yes)
6. `AKUN-006-WPENG-VLESS-WS-93MS` (url=292ms, nekobox=236ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-101MS` (url=261ms, nekobox=243ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-117MS` (url=221ms, nekobox=206ms, status=no)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-105MS` (url=262ms, nekobox=237ms, status=no)
10. `AKUN-008-CLOUDFLARE-VLESS-WS-115MS`
11. `AKUN-009-466688-VLESS-WS-117MS`
12. `AKUN-010-CLOUDFLARE-VLESS-WS-108MS`
13. `AKUN-013-BGP48-HK-VLESS-WS-117MS` (url=236ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-134MS` (url=220ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-147MS` (url=289ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-134MS` (url=274ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-126MS` (url=302ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-161MS` (url=273ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-162MS` (url=266ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-130MS` (url=289ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-256MS` (url=287ms, status=HTTP 204)
22. `AKUN-024-CLOUDFLARE-VLESS-WS-404MS` (url=824ms, status=HTTP 204)
23. `AKUN-025-UNKNOWN-VLESS-WS-399MS` (url=780ms, status=HTTP 204)
24. `AKUN-026-UNKNOWN-VLESS-WS-435MS` (url=2130ms, status=HTTP 204)
25. `AKUN-028-UNKNOWN-VLESS-WS-711MS` (url=1225ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
