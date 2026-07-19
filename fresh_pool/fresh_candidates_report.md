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
- Proxy di openclash_fresh_pool.yaml: 30

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-89MS` (url=203ms, nekobox=247ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-89MS` (url=203ms, nekobox=241ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-86MS` (url=217ms, nekobox=237ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-99MS` (url=219ms, nekobox=246ms, status=yes)
5. `AKUN-005-SAVVY-7-VLESS-WS-93MS` (url=217ms, nekobox=292ms, status=yes)
6. `AKUN-006-OVH-VLESS-WS-107MS` (url=230ms, nekobox=492ms, status=yes)
7. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-110MS` (url=210ms, nekobox=234ms, status=yes)
8. `AKUN-008-POLICE-VLESS-WS-112MS` (url=289ms, nekobox=291ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-116MS` (url=204ms, nekobox=235ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-120MS` (url=212ms, nekobox=237ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-126MS` (url=278ms, status=HTTP 204)
12. `AKUN-012-UK-GB-DCL-01-20191003-VLESS-WS-117MS` (url=237ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-92MS` (url=238ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-126MS` (url=209ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-138MS` (url=232ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-141MS` (url=241ms, status=HTTP 204)
17. `AKUN-017-UK-GB-DCL-01-20191003-VLESS-WS-142MS` (url=284ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-117MS` (url=223ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-152MS` (url=208ms, status=HTTP 204)
20. `AKUN-020-466688-VLESS-WS-91MS` (url=220ms, status=HTTP 204)
21. `AKUN-021-UK-GB-DCL-01-20191003-VLESS-WS-134MS` (url=268ms, status=HTTP 204)
22. `AKUN-022-US-VLESS-WS-145MS` (url=245ms, status=HTTP 204)
23. `AKUN-023-ZVC-VLESS-WS-96MS` (url=230ms, status=HTTP 204)
24. `AKUN-024-WPENG-VLESS-WS-175MS` (url=228ms, status=HTTP 204)
25. `AKUN-025-RS-RAPIDSEEDBOX-20190717-VLESS-WS-210MS` (url=328ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
