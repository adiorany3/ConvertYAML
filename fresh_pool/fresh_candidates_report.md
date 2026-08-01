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
1. `AKUN-001-OVH-VLESS-WS-83MS` (url=214ms, nekobox=262ms, status=yes)
2. `AKUN-002-877774-VLESS-WS-86MS` (url=237ms, nekobox=257ms, status=yes)
3. `AKUN-003-877774-VLESS-WS-89MS` (url=205ms, nekobox=266ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-87MS` (url=206ms, nekobox=234ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-95MS` (url=235ms, nekobox=259ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-94MS` (url=234ms, nekobox=265ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-91MS` (url=210ms, nekobox=263ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-96MS` (url=209ms, nekobox=309ms, status=yes)
9. `AKUN-009-LEVIKOGJGFDD-VLESS-WS-102MS` (url=224ms, nekobox=238ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-108MS` (url=219ms, nekobox=268ms, status=yes)
11. `AKUN-012-CLOUDFLARE-VLESS-WS-321MS` (url=623ms, status=HTTP 204)
12. `AKUN-015-CLOUDFLARE-VLESS-WS-623MS` (url=1267ms, status=HTTP 204)
13. `AKUN-017-CLOUDFLARE-VLESS-WS-682MS` (url=1119ms, status=HTTP 204)
14. `AKUN-018-UNKNOWN-VLESS-WS-704MS` (url=1113ms, status=HTTP 204)
15. `AKUN-020-CLOUDFLARE-VLESS-WS-644MS` (url=1029ms, status=HTTP 204)
16. `AKUN-021-UNKNOWN-VLESS-WS-734MS` (url=1167ms, status=HTTP 204)
17. `AKUN-023-UNKNOWN-VLESS-WS-689MS` (url=1108ms, status=HTTP 204)
18. `AKUN-024-AS199785-DE-IPV4-VLESS-WS-740MS` (url=1202ms, status=HTTP 204)
19. `AKUN-026-AS199785-DE-IPV4-VLESS-WS-756MS` (url=1211ms, status=HTTP 204)
20. `AKUN-027-CLOUDFLARE-VLESS-WS-755MS` (url=1192ms, status=HTTP 204)
21. `AKUN-028-CLOUDFLARE-VLESS-WS-816MS` (url=4162ms, status=HTTP 204)
22. `AKUN-030-CLOUDFLARE-VLESS-WS-794MS` (url=1877ms, status=HTTP 204)
23. `AKUN-035-CLOUDFLARE-VLESS-WS-794MS` (url=3038ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
