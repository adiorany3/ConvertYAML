# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 21
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 25

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-109MS` (url=363ms, nekobox=300ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-120MS` (url=341ms, nekobox=290ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-126MS` (url=248ms, nekobox=271ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-123MS` (url=276ms, nekobox=319ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-145MS`
6. `AKUN-006-UNKNOWN-VLESS-WS-124MS`
7. `AKUN-007-LEVIKOGJGFDD-VLESS-WS-116MS`
8. `AKUN-008-UNKNOWN-VLESS-WS-170MS`
9. `AKUN-009-UNKNOWN-VLESS-WS-189MS`
10. `AKUN-010-UNKNOWN-VLESS-WS-177MS`
11. `AKUN-012-UNKNOWN-VLESS-WS-160MS` (url=303ms, status=HTTP 204)
12. `AKUN-014-CLOUDFLARE-VLESS-WS-190MS` (url=238ms, status=HTTP 204)
13. `AKUN-015-CLOUDFLARE-VLESS-WS-170MS` (url=251ms, status=HTTP 204)
14. `AKUN-016-CLOUDFLARE-VLESS-WS-280MS` (url=697ms, status=HTTP 204)
15. `AKUN-020-CLOUDFLARE-VLESS-WS-285MS` (url=445ms, status=HTTP 204)
16. `AKUN-022-CLOUDFLARE-VLESS-WS-495MS` (url=831ms, status=HTTP 204)
17. `AKUN-024-CLOUDFLARE-VLESS-WS-472MS` (url=1426ms, status=HTTP 204)
18. `AKUN-027-CLOUDFLARE-VLESS-WS-561MS` (url=972ms, status=HTTP 204)
19. `AKUN-030-CLOUDFLARE-VLESS-WS-616MS` (url=1081ms, status=HTTP 204)
20. `AKUN-033-UNKNOWN-VLESS-WS-599MS` (url=1403ms, status=HTTP 204)
21. `AKUN-034-CLOUDFLARE-VLESS-WS-722MS` (url=1016ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
