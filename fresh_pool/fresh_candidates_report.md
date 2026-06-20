# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 17
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 23

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
1. `AKUN-001-SPEEDTEST-VLESS-WS-73MS` (url=224ms, nekobox=217ms, status=no)
2. `AKUN-001-CLOUDFLARE-VLESS-WS-102MS`
3. `AKUN-002-CLOUDFLARE-VLESS-WS-272MS`
4. `AKUN-003-CLOUDFLARE-VLESS-WS-243MS`
5. `AKUN-004-CLOUDFLARE-VLESS-WS-294MS`
6. `AKUN-005-RS-RAPIDSEEDBOX-20190717-VLESS-WS-73MS`
7. `AKUN-012-CLOUDFLARE-VLESS-WS-374MS` (url=634ms, nekobox=487ms, status=no)
8. `AKUN-006-CONFLU-VLESS-WS-228MS`
9. `AKUN-007-CLOUDFLARE-VLESS-WS-92MS`
10. `AKUN-017-CLOUDFLARE-VLESS-WS-369MS` (url=561ms, nekobox=489ms, status=no)
11. `AKUN-018-CLOUDFLARE-VLESS-WS-383MS` (url=579ms, nekobox=487ms, status=no)
12. `AKUN-020-CLOUDFLARE-VLESS-WS-370MS` (url=579ms, nekobox=501ms, status=no)
13. `AKUN-027-CLOUDFLARE-VLESS-WS-376MS` (url=594ms, nekobox=509ms, status=no)
14. `AKUN-008-CLOUDFLARE-VLESS-WS-278MS`
15. `AKUN-029-UNKNOWN-VLESS-WS-496MS` (url=886ms, nekobox=604ms, status=no)
16. `AKUN-009-UNKNOWN-VLESS-WS-483MS`
17. `AKUN-010-UNKNOWN-VLESS-WS-694MS`

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
