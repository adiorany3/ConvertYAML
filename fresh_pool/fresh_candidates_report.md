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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-131MS` (url=258ms, nekobox=320ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-141MS` (url=268ms, nekobox=291ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-145MS` (url=328ms, nekobox=316ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-142MS` (url=276ms, nekobox=298ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-138MS` (url=263ms, nekobox=294ms, status=yes)
6. `AKUN-006-PUBLICDOMAINREGISTRY-NET-VLESS-WS-149MS` (url=315ms, nekobox=375ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-150MS` (url=282ms, nekobox=314ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-160MS` (url=285ms, nekobox=315ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-168MS` (url=289ms, nekobox=300ms, status=yes)
10. `AKUN-010-RS-RAPIDSEEDBOX-20190717-VLESS-WS-165MS` (url=261ms, nekobox=296ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-156MS` (url=310ms, status=HTTP 204)
12. `AKUN-012-ZVC-VLESS-WS-169MS` (url=304ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-158MS` (url=350ms, status=HTTP 204)
14. `AKUN-014-WEBEX-VLESS-WS-157MS` (url=320ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-150MS` (url=289ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-186MS` (url=252ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-176MS` (url=299ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-289MS` (url=481ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-382MS` (url=708ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-392MS` (url=782ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-390MS` (url=800ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-149MS` (url=316ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-375MS` (url=728ms, status=HTTP 204)
24. `AKUN-027-UNKNOWN-VLESS-WS-662MS` (url=1030ms, status=HTTP 204)
25. `AKUN-030-UNKNOWN-VLESS-WS-700MS` (url=1243ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
