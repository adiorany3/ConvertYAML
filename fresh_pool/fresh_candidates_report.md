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
1. `AKUN-001-UNKNOWN-VLESS-WS-88MS` (url=209ms, nekobox=236ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-90MS` (url=204ms, nekobox=228ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-92MS` (url=204ms, nekobox=238ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-89MS` (url=201ms, nekobox=230ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-88MS` (url=207ms, nekobox=245ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-94MS` (url=206ms, nekobox=243ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-93MS` (url=220ms, nekobox=237ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-103MS` (url=221ms, nekobox=239ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-94MS` (url=208ms, nekobox=244ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-115MS` (url=208ms, nekobox=248ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-96MS` (url=206ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-118MS` (url=232ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-134MS` (url=228ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-136MS` (url=275ms, status=HTTP 204)
15. `AKUN-015-WPENG-VLESS-WS-112MS` (url=239ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-142MS` (url=214ms, status=HTTP 204)
17. `AKUN-017-DIXONS-VLESS-WS-114MS` (url=221ms, status=HTTP 204)
18. `AKUN-019-466688-VLESS-WS-151MS` (url=209ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-171MS` (url=350ms, status=HTTP 204)
20. `AKUN-022-CLOUDFLARE-VLESS-WS-127MS` (url=251ms, status=HTTP 204)
21. `AKUN-023-CLOUDFLARE-VLESS-WS-123MS` (url=241ms, status=HTTP 204)
22. `AKUN-024-CLOUDFLARE-VLESS-WS-140MS` (url=244ms, status=HTTP 204)
23. `AKUN-025-UK-GB-DCL-01-20191003-VLESS-WS-134MS` (url=273ms, status=HTTP 204)
24. `AKUN-026-CLOUDFLARE-VLESS-WS-381MS` (url=772ms, status=HTTP 204)
25. `AKUN-027-CLOUDFLARE-VLESS-WS-382MS` (url=811ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
